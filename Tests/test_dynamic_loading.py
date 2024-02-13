import unittest
from Tests.base_test import BaseTest
from Pages.dynamic_loading_page import DynamicLoadingPageOne, DynamicLoadingPageTwo
from Resources.locators import DynamicLoadingLocators

class TestDynamicLoading(BaseTest):
    def setUp(self):
        super().setUp()
        self.dynamic_loading_page1 = DynamicLoadingPageOne(self.driver)
        self.dynamic_loading_page2 = DynamicLoadingPageTwo(self.driver)

    def testDynamicLoading1(self):
        #Check if message is invisible, click start button, check that message is visible after loading
        self.assertFalse(self.dynamic_loading_page1.checkVisiblity(DynamicLoadingLocators.Finish))

        self.dynamic_loading_page1.clickStart()
        self.assertTrue(self.dynamic_loading_page1.checkVisiblity(DynamicLoadingLocators.Finish))

    def testDynamicLoading2(self):
        #Check if message is not present, click start button, check that message is present after loading
        self.assertFalse(self.dynamic_loading_page2.checkPresence(DynamicLoadingLocators.Finish))

        self.dynamic_loading_page2.clickStart()
        self.assertTrue(self.dynamic_loading_page2.checkPresence(DynamicLoadingLocators.Finish))

if __name__ == "__main__":
    unittest.main()