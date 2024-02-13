import unittest
from Tests.base_test import BaseTest
from Pages.exit_intent_page import ExitIntentPage
from Resources.locators import ExitIntentLocators

class TestExitIntent(BaseTest):
    def setUp(self):
        super().setUp()
        self.exit_intent_page = ExitIntentPage(self.driver)

    def testExitWindow(self):
        #Verify modal window is not visible yet
        self.assertFalse(self.exit_intent_page.checkVisiblity(ExitIntentLocators.ModalWindow))

        #Move mouse to the top right corner of the window and verify that the modal window is now visible
        self.exit_intent_page.hoverOutOfViewportPane()
        self.assertTrue(self.exit_intent_page.checkVisiblity(ExitIntentLocators.ModalWindow))

        #Close the modal window and verify that it is invisible again
        self.exit_intent_page.click(ExitIntentLocators.Close)
        self.assertFalse(self.exit_intent_page.checkVisiblity(ExitIntentLocators.ModalWindow))

if __name__ == "__main__":
    unittest.main()