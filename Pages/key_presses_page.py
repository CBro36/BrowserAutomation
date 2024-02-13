from Pages.base_page import BasePage
from Resources.locators import KeyPressesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class KeyPressesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/key_presses')

    def inputKey(self, keyInput):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(KeyPressesLocators.Target)).send_keys(keyInput)