from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

class ChallengingDOMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/challenging_dom")

    #Get canvas number from html and regex matching
    def getCanvasNum(self, locator):
        innerHTML = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator)).get_attribute("innerHTML")
        return re.search(r"Answer:\s(\d+)", innerHTML).group(1)