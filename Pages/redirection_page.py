from Pages.base_page import BasePage
import requests

class RedirectionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.r = requests.get('https://the-internet.herokuapp.com/redirect')

    def getURL(self):
        return self.r.url
    
    def getSC(self):
        return self.r.status_code
    
    def getHistory(self):
        return self.r.history