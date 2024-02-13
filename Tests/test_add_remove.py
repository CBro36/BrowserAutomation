import unittest
from Tests.base_test import BaseTest
from Pages.add_remove_page import AddRemovePage
from Resources.locators import AddRemoveLocators

class testAddRemove(BaseTest):
    def setUp(self):
        super().setUp()
        self.add_remove_page = AddRemovePage(self.driver)

    def testButtons(self):
        #Click add, check if delete button is there, click delete, check if delete button is gone
        self.add_remove_page.click(AddRemoveLocators.AddButton)
        self.add_remove_page.checkVisiblity(AddRemoveLocators.DeleteButton)
        self.add_remove_page.click(AddRemoveLocators.DeleteButton)
        self.add_remove_page.checkVisiblity(AddRemoveLocators.DeleteButton)

if __name__ == "__main__":
    unittest.main()