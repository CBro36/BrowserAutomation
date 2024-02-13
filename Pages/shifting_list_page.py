from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Resources.locators import ShiftingListLocators

class ShiftingListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/shifting_content/list')

    def getLines(self):
        #Returns lines of text in the list
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(ShiftingListLocators.List)).get_attribute("innerHTML").splitlines()