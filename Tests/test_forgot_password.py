import unittest
from Tests.base_test import BaseTest
from Pages.forgot_password_page import ForgotPasswordPage
from Resources.locators import ForgotPasswordLocators

class TestForgotPassword(BaseTest):
    def setUp(self):
        super().setUp()
        self.forgot_pwd_page = ForgotPasswordPage(self.driver)

    def testPwdRetrieval(self):
        #Input email to text field and click submit button
        self.forgot_pwd_page.inputEmail('admin@example.com')
        self.forgot_pwd_page.click(ForgotPasswordLocators.SubmitButton)
        #Since there's no real password retrieval, clicking submit just gets a 500 status code response
        self.assertIn('Internal Server Error', self.driver.page_source)

if __name__ == "__main__":
    unittest.main()