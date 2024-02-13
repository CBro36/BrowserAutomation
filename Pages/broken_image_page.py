from Pages.base_page import BasePage
from Resources.locators import BrokenImageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BrokenImagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/broken_images")

    #Returns all elements on the page with the img tag
    def getImages(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(BrokenImageLocators.Images))