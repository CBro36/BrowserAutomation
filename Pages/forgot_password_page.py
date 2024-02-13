from Pages.base_page import BasePage
from Resources.locators import ForgotPasswordLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/forgot_password')

    def inputEmail(self, email):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(ForgotPasswordLocators.EmailInput)).send_keys(email)