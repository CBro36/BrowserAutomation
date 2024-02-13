from Pages.base_page import BasePage
from Resources.locators import CheckboxesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CheckboxesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

    #Checks if checkbox is selected or not
    def getStatus(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).is_selected()