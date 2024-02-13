import unittest
from Tests.base_test import BaseTest
from Pages.context_menu_page import ContextMenuPage
from Resources.locators import ContextMenuLocators
from selenium.common.exceptions import TimeoutException

class TestContextMenu(BaseTest):
    def setUp(self):
        super().setUp()
        self.context_menu_page = ContextMenuPage(self.driver)
    
    def testContextMenu(self):
        #Right clicks the element and accepts the alert pop up
        self.context_menu_page.rightClick(ContextMenuLocators.Box)
        try:
            self.context_menu_page.handleAlert()
        except TimeoutException:
            print("No alert")

if __name__ == "__main__":
    unittest.main()