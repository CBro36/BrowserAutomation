import unittest
from Tests.base_test import BaseTest
from Pages.input_page import InputPage
from Resources.locators import InputLocators

class TestInput(BaseTest):
    def setUp(self):
        super().setUp()
        self.input_page = InputPage(self.driver)

    def testInput(self):
        #These tests input various values, verify the correct value displays, and clears the input field
        self.input_page.inputNum('5')
        self.assertEqual(self.input_page.getAttribute(InputLocators.InputField, "value"), '5')
        self.input_page.clearField()

        self.input_page.inputNum('10')
        self.assertEqual(self.input_page.getAttribute(InputLocators.InputField, "value"), '10')
        self.input_page.clearField()

        self.input_page.inputNum('100')
        self.assertEqual(self.input_page.getAttribute(InputLocators.InputField, "value"), '100')
        self.input_page.clearField()

if __name__ == "__main__":
    unittest.main()