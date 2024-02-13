import unittest
from Tests.base_test import BaseTest
from Pages.form_authentication_page import FormAuthenticationPage
from Resources.locators import FormAuthenticationLocators

class TestFormAuthentication(BaseTest):
    def setUp(self):
        super().setUp()
        self.form_auth_page = FormAuthenticationPage(self.driver)

    def testSuccessfulLogin(self):
        #Input correct credentials, click login button, and verify the login success message displays
        self.form_auth_page.inputCredentials('tomsmith', 'SuperSecretPassword!')
        self.form_auth_page.click(FormAuthenticationLocators.LoginButton)
        self.assertEqual(self.form_auth_page.getMessage(FormAuthenticationLocators.Message), "You logged into a secure area!")

        #Click logout and verify the logout message displays
        self.form_auth_page.click(FormAuthenticationLocators.LogoutButton)
        self.assertEqual(self.form_auth_page.getMessage(FormAuthenticationLocators.Message), "You logged out of the secure area!")

    def testFailedLogin(self):
        #Input incorrect username, click login, verify that appropriate error message displays
        self.form_auth_page.inputCredentials('wrong', 'SuperSecretPassword!')
        self.form_auth_page.click(FormAuthenticationLocators.LoginButton)
        self.assertEqual(self.form_auth_page.getMessage(FormAuthenticationLocators.Message), "Your username is invalid!")

        #Performs the same test but with an incorrect password
        self.form_auth_page.inputCredentials('tomsmith', 'wrong')
        self.form_auth_page.click(FormAuthenticationLocators.LoginButton)
        self.assertEqual(self.form_auth_page.getMessage(FormAuthenticationLocators.Message), "Your password is invalid!")

if __name__ == "__main__":
    unittest.main()