from Pages.base_page import BasePage
from Resources.locators import DynamicControlsLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DynamicControlsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/dynamic_controls')

    def clickButton(self, locator):
        #Click button and wait for loading bar to disappear
        self.click(locator)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DynamicControlsLocators.LoadingBar))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(DynamicControlsLocators.LoadingBar))
        
    def checkTextInput(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DynamicControlsLocators.TextInput)).is_enabled()
    
    def inputText(self, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DynamicControlsLocators.TextInput)).send_keys(text)