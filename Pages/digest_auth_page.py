from Pages.base_page import BasePage
import requests
from requests.auth import HTTPDigestAuth
import autoit

class DigestAuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Create session and get website with digest auth credentials
        #Get site with webdriver and pass the session's auth cookies to the driver
        session = requests.Session()
        www_request = session.get('https://the-internet.herokuapp.com/digest_auth', auth=HTTPDigestAuth('admin', 'admin'))
        self.driver.get('https://the-internet.herokuapp.com/digest_auth')

        cookies = session.cookies.get_dict()
        for key in cookies:
            self.driver.add_cookie({'name': key, 'value': cookies[key]})

        self.driver.get('https://the-internet.herokuapp.com/digest_auth')

    def enterCredentials(self):
        #Input credentials into authentication alert
        autoit.win_wait_active("", 10)
        autoit.send("admin{TAB}")
        autoit.send("admin{ENTER}")