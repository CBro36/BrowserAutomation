import unittest
from Tests.base_test import BaseTest
from Pages.multiple_windows_page import MultipleWindowsPage
from Resources.locators import MultipleWindowsLocators

class TestMultipleWindows(BaseTest):
    def setUp(self):
        super().setUp()
        self.multi_window_page = MultipleWindowsPage(self.driver)

    def testMultipleWindows(self):
        #Open the new window and verify the driver has switched to it
        self.multi_window_page.click(MultipleWindowsLocators.Link)
        self.multi_window_page.switchWindows()
        self.assertIn('New Window', self.driver.page_source)

if __name__ == "__main__":
    unittest.main()