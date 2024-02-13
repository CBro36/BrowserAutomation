import unittest
from Pages.horizontal_slider_page import HorizontalSliderPage
from Resources.locators import HorizontalSliderLocators
from Tests.base_test import BaseTest

class TestHorizontalSlider(BaseTest):
    def setUp(self):
        super().setUp()
        self.h_slider_page = HorizontalSliderPage(self.driver)

    def testClickNDrag(self):
        #Tests different values using click and drag actions and verifies the correct value is displayed 
        self.h_slider_page.dragSlider(2.5, 5, 0)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '2.5')

        self.h_slider_page.dragSlider(5, 5, 0)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '5')

        self.h_slider_page.dragSlider(0, 5, 0)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '0')

    def testArrowKeys(self):
        #The same as the first test but uses arrow key inputs
        self.h_slider_page.useArrowKeys('right', 5)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '2.5')

        self.h_slider_page.useArrowKeys('right', 5)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '5')

        self.h_slider_page.useArrowKeys('left', 10)
        self.assertEqual(self.h_slider_page.getText(HorizontalSliderLocators.Value), '0')

if __name__ == "__main__":
    unittest.main()