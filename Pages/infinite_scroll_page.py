from Pages.base_page import BasePage
from Resources.locators import InfiniteScrollLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class InfiniteScrollPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/infinite_scroll')

    def countSegments(self):
        #Returns the number of paragraph segements currently on the page
        return len(WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(InfiniteScrollLocators.Segments)))
    
    def scrollToBottom(self):
        #Scrolls to the botton of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);")
        time.sleep(0.5)