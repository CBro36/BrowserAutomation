import unittest
from Tests.base_test import BaseTest
from Pages.large_and_deep_dom_page import LargeAndDeepDOMPage
from Resources.locators import LargeAndDeepDOMLocators

class TestLargeAndDeepDOM(BaseTest):
    def setUp(self):
        super().setUp()
        self.large_dom_page = LargeAndDeepDOMPage(self.driver)

    def testDOM(self):
        #Verifies that arbitrary elements display the correct values
        self.large_dom_page.scrollToElement(LargeAndDeepDOMLocators.Sib25_3)
        self.assertEqual(self.large_dom_page.getText(LargeAndDeepDOMLocators.Sib25_3), '25.3')

        self.large_dom_page.scrollToElement(LargeAndDeepDOMLocators.Sib50_2)
        self.assertEqual(self.large_dom_page.getText(LargeAndDeepDOMLocators.Sib50_2), '50.2')

        self.large_dom_page.scrollToElement(LargeAndDeepDOMLocators.TableElem)
        self.assertEqual(self.large_dom_page.getText(LargeAndDeepDOMLocators.TableElem), '47.12')

if __name__ == "__main__":
    unittest.main()