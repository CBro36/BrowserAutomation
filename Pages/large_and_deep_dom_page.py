from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LargeAndDeepDOMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/large')
        self.driver.maximize_window()

    def scrollToElement(self, locator):
        #Scrolls until the specified element is in view since not all elements are able to fit on screen
        elem = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        self.actionChains.move_to_element(elem).perform()