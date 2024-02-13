import unittest
from Tests.base_test import BaseTest
from Pages.entry_ad_page import EntryAdPage
from Resources.locators import EntryAdLocators

class TestEntryAd(BaseTest):
    def setUp(self):
        super().setUp()
        self.entry_ad_page = EntryAdPage(self.driver)

    def testModalWindow(self):
        #Verify modal window is visible on page load
        self.assertTrue(self.entry_ad_page.checkVisiblity(EntryAdLocators.ModalWindow))

        #Close the window and verify the window is no longer visible
        self.entry_ad_page.click(EntryAdLocators.Close)
        self.assertFalse(self.entry_ad_page.checkVisiblity(EntryAdLocators.ModalWindow))

if __name__ == "__main__":
    unittest.main()