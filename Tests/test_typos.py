import unittest
from Tests.base_test import BaseTest
from Pages.typos_page import TyposPage
from Resources.locators import TyposLocators

class TestTypos(BaseTest):
    def setUp(self):
        super().setUp()
        self.typos_page = TyposPage(self.driver)

    def testTypos(self):
        expected = """Typos
        This example demonstrates a typo being introduced. It does it randomly on each page load.
        Sometimes you'll see a typo, other times you won't."""
        expectedList = self.typos_page.getWords(text=expected)
        words = self.typos_page.getWords(locator=TyposLocators.TextBody)

        #Compare each word of the expected text and the page text to see if there's a typo
        for e, w in zip(expectedList, words):
            if w != e:
                print("Typo found: " + w + " -> " + e)

if __name__ == "__main__":
    unittest.main()