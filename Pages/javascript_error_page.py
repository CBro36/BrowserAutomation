from Pages.base_page import BasePage
from selenium.common.exceptions import WebDriverException

class JavaScriptErrorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/javascript_error')

    def getLogs(self):
        #Gets any errors from the webdriver's browser logs
        try:
            browserLogs = self.driver.get_log('browser')
        except (ValueError, WebDriverException) as e:
            print("Could not get browser logs due to exception %s", e)
            return []
        
        errors = [entry for entry in browserLogs if entry['level'] == 'SEVERE']
        return errors