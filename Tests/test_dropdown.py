import unittest
from Tests.base_test import BaseTest
from Pages.dropdown_page import DropdownPage

class TestDropdown(BaseTest):
    def setUp(self):
        super().setUp()
        self.dropdown_page = DropdownPage(self.driver)

    def testDropdown(self):
        #Selects different options and verifies that they are selected
        self.dropdown_page.selectOption("Option 1")
        self.assertEqual(self.dropdown_page.getSelectedOptions()[0].text, "Option 1")

        self.dropdown_page.selectOption("Option 2")
        self.assertEqual(self.dropdown_page.getSelectedOptions()[0].text, "Option 2")

if __name__ == "__main__":
    unittest.main()