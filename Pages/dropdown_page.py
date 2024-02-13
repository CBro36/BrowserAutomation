from Pages.base_page import BasePage
from Resources.locators import DropdownLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class DropdownPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        self.select = Select(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(DropdownLocators.Dropdown)))

    def selectOption(self, option):
        self.select.select_by_visible_text(option)

    def getSelectedOptions(self):
        return self.select.all_selected_options