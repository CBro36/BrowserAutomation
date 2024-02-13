import unittest
from Tests.base_test import BaseTest
from Pages.digest_auth_page import DigestAuthPage

class TestDigestAuth(BaseTest):
    def setUp(self):
        super().setUp()
        self.digest_auth_page = DigestAuthPage(self.driver)

    def testDigestAuth(self):
        self.digest_auth_page.enterCredentials()
        #Verify the login was successful
        self.assertIn("Congratulations! You must have the proper credentials.", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()