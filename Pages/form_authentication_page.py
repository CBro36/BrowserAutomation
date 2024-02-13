from Pages.base_page import BasePage
from Resources.locators import FormAuthenticationLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FormAuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/login')

    def inputCredentials(self, username, password):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(FormAuthenticationLocators.Username)).send_keys(username)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(FormAuthenticationLocators.Password)).send_keys(password)

    def getMessage(self, locator):
        #Returns the text inside of the flash notification at the top of the page
        return self.getAttribute(locator, "innerHTML").splitlines()[1].strip()