from Pages.base_page import BasePage

class StatusCodesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/status_codes')

    def getStatusCode(self):
        return self.driver.last_request.url, self.driver.last_request.response.status_code