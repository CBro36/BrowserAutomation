from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContextMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")

    #Switches to alert and accepts it
    def handleAlert(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()