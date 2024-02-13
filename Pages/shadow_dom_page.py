from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ShadowDOMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/shadowdom')

    def switchToShadow(self, locator):
        #Returns the shadow root of the shadow host
        shadowHost = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        return shadowHost.shadow_root
    
    def getShadowElem(self, root, locator):
        return WebDriverWait(root, 3).until(EC.visibility_of_element_located(locator)).text