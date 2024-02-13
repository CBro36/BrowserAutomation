from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HoversPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/hovers')

    def mouseOverImg(self, locator):
        #Gets an image element and hovers the mouse over it
        img = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.actionChains.move_to_element(img).perform()