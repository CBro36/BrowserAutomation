from Pages.base_page import BasePage
from Resources.locators import WYSIWYGEditorLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WYSIWYGEditorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/tinymce')

    def switchToEditor(self):
        #Switches to the editor's iframe to access its elements
        iframe = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(WYSIWYGEditorLocators.Editor))
        self.driver.switch_to.frame(iframe)

    def clearText(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(WYSIWYGEditorLocators.TextBox)).clear()

    def sendText(self, text):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(WYSIWYGEditorLocators.TextBox)).send_keys(text)