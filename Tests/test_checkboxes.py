import unittest
from Tests.base_test import BaseTest
from Pages.checkboxes_page import CheckboxesPage
from Resources.locators import CheckboxesLocators

class TestCheckboxes(BaseTest):
    def setUp(self):
        super().setUp()
        self.checkboxes_page = CheckboxesPage(self.driver)

    def testButtons(self):
        #Click the first checkbox and verify that it's checked
        self.checkboxes_page.click(CheckboxesLocators.Checkbox1)
        self.assertTrue(self.checkboxes_page.getStatus(CheckboxesLocators.Checkbox1))
        
        #Click the second checkbox and verify that it's unchecked
        self.checkboxes_page.click(CheckboxesLocators.Checkbox2)
        self.assertFalse(self.checkboxes_page.getStatus(CheckboxesLocators.Checkbox2))

if __name__ == "__main__":
    unittest.main()