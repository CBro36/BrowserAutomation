from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class JQueryUIMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/jqueryui/menu')

    def mouseOver(self, locator):
        #Hovers the mouse over the specified element
        elem = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.actionChains.move_to_element(elem).perform()