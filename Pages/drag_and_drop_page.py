from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DragAndDropPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def dnd(self, source, target):
        #Uses action chains to drag and drop the source to the target
        elem1 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(source))
        elem2 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(target))
        self.actionChains.drag_and_drop(elem1, elem2).perform()