from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import base64

#Base Page functionality that all other page classes will extend
class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.actionChains = ActionChains(self.driver)
        self.bauth = base64.b64encode(("admin:admin").encode('ascii')) 

    #Adds header for basic authentication requests
    def interceptorBasic(self, req):
        req.headers['Authorization'] = 'Basic ' + self.bauth.decode('ascii')

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()  

    def rightClick(self, locator):
          self.actionChains.context_click(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))).perform()

    def checkVisiblity(self, locator):
         try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
         except TimeoutException:
             return False
         
         return True
         
    def checkPresence(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        except TimeoutException:
             return False
        
        return True
        
    def getText(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text
    
    def getAttribute(self, locator, attribute):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).get_attribute(attribute)