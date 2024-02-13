from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ShiftingMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/shifting_content/menu')

    def getLocation(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).location