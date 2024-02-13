import unittest
from Tests.base_test import BaseTest
from Pages.shifting_menu_page import ShiftingMenuPage
from Resources.locators import ShiftingMenuLocators

class TestShiftingMenu(BaseTest):
    def setUp(self):
        super().setUp()
        self.shift_menu_page = ShiftingMenuPage(self.driver)

    def testMenu(self):
        #Record first location of button then refresh page
        location1 = self.shift_menu_page.getLocation(ShiftingMenuLocators.Gallery)
        self.driver.refresh()

        #Record second location of button and verify the button shifted on the x axis
        location2 = self.shift_menu_page.getLocation(ShiftingMenuLocators.Gallery)
        self.assertNotEqual(location1['x'], location2['x'])

if __name__ == "__main__":
    unittest.main()