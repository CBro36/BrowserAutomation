from Pages.base_page import BasePage

class BasicAuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Intercept the request with our basic authentication authorization header with our credentials
        self.driver.request_interceptor = self.interceptorBasic
        self.driver.get('https://the-internet.herokuapp.com/basic_auth')