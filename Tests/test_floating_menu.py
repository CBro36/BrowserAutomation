import unittest
from Tests.base_test import BaseTest
from Pages.floating_menu_page import FloatingMenuPage
from Resources.locators import FloatingMenuLocators

class TestFloatingMenu(BaseTest):
    def setUp(self):
        super().setUp()
        self.float_menu_page = FloatingMenuPage(self.driver)

    def testMenu(self):
        """Each button simply appends the name of the last clicked button to the url after the #.
        This test clicks each button and verifies the url changed properly."""
        self.float_menu_page.click(FloatingMenuLocators.HomeButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/floating_menu#home')

        self.float_menu_page.click(FloatingMenuLocators.NewsButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/floating_menu#news')

        self.float_menu_page.click(FloatingMenuLocators.ContactButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/floating_menu#contact')

        self.float_menu_page.click(FloatingMenuLocators.AboutButton)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/floating_menu#about')

if __name__ == "__main__":
    unittest.main()