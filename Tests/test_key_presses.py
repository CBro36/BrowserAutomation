import unittest
from Tests.base_test import BaseTest
from Pages.key_presses_page import KeyPressesPage
from Resources.locators import KeyPressesLocators
from selenium.webdriver.common.keys import Keys

class TestKeyPresses(BaseTest):
    def setUp(self):
        super().setUp()
        self.key_presses_page = KeyPressesPage(self.driver)

    def processKey(self, key, expected):
        #Input a key press and verify the resulting string displays the correct information
        self.key_presses_page.inputKey(key)
        self.assertEqual(self.key_presses_page.getText(KeyPressesLocators.Result), expected)
    
    def testKeys(self):
        self.processKey(Keys.CONTROL, "You entered: CONTROL")
        self.processKey(Keys.SHIFT, "You entered: SHIFT")
        self.processKey(Keys.TAB, "You entered: TAB")
        self.processKey(Keys.ESCAPE, "You entered: ESCAPE")
        self.processKey(Keys.SPACE, "You entered: SPACE")
        self.processKey(Keys.BACK_SPACE, "You entered: BACK_SPACE")

        #Inputting enter sends you to the same page but with a '?' appended to the URL
        self.key_presses_page.inputKey(Keys.ENTER)
        self.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/key_presses?")

if __name__ == "__main__":
    unittest.main()