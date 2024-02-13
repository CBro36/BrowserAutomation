from Pages.base_page import BasePage

class SecureDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Use basic auth interceptor for request
        self.driver.request_interceptor = self.interceptorBasic
        self.driver.get('https://the-internet.herokuapp.com/download_secure')