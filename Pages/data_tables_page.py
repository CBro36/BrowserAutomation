from Pages.base_page import BasePage
from Resources.locators import DataTablesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DataTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/tables')

    def getRows(self, locator):
        #Locates and returns the rows of the table
        table = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        body = table.find_element(*(DataTablesLocators.Tbody))
        return body.find_elements(*(DataTablesLocators.Trows))

    def getColumn(self, locator):
        #Returns one column from a table
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))