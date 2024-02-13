from Pages.base_page import BasePage
from Resources.locators import NotificationMessageLocators

class NotificationMessagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/notification_message_rendered')

    def getMessage(self):
        #Returns the text inside of the flash notification at the top of the page
        return self.getAttribute(NotificationMessageLocators.Message, "innerHTML").splitlines()[1].strip()