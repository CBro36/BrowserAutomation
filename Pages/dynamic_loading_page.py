from Pages.base_page import BasePage
from Resources.locators import DynamicLoadingLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DynamicLoadingPageBase(BasePage):
    def clickStart(self):
        #CLick start button and wait for loading bar to disappear
        self.click(DynamicLoadingLocators.Start)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DynamicLoadingLocators.LoadingBar))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(DynamicLoadingLocators.LoadingBar))

class DynamicLoadingPageOne(DynamicLoadingPageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
        
class DynamicLoadingPageTwo(DynamicLoadingPageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')