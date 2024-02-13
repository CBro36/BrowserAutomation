import unittest
from Tests.base_test import BaseTest
from Pages.notification_message_page import NotificationMessagePage
from Resources.locators import NotificationMessageLocators

class TestNotificationMessage(BaseTest):
    def setUp(self):
        super().setUp()
        self.notif_message_page = NotificationMessagePage(self.driver)

    def testNotifMessage(self):
        #Loop for 10 iterations clicking the button and printing the notification message
        for i in range(10):
            self.notif_message_page.click(NotificationMessageLocators.Link)
            print(self.notif_message_page.getMessage())

if __name__ == "__main__":
    unittest.main()