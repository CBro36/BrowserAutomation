import unittest
from Tests.base_test import BaseTest
from Pages.redirection_page import RedirectionPage

class TestRedirection(BaseTest):
    def setUp(self):
        super().setUp()
        self.redirection_page = RedirectionPage(self.driver)

    def testRedirection(self):
        #Verify we were sent to the redirect URL with the correct status code
        self.assertEqual(self.redirection_page.getURL(), 'https://the-internet.herokuapp.com/status_codes')
        self.assertEqual(self.redirection_page.getSC(), 200)
        print(self.redirection_page.getHistory())

if __name__ == "__main__":
    unittest.main()