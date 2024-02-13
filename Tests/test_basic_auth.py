import unittest
from Tests.base_test import BaseTest
from Pages.basic_auth_page import BasicAuthPage

class testBasicAuth(BaseTest):
    def setUp(self):
        super().setUp(driverType='wire')
        self.basic_auth_page = BasicAuthPage(self.driver)

    def testAuth(self):
        #Verify that we logged in correctly
        self.assertIn("Congratulations! You must have the proper credentials.", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()