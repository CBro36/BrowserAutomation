import unittest
from Tests.base_test import BaseTest
from Pages.shifting_image_page import ShiftingImagePage
from Resources.locators import ShiftingImageLocators

class TestShiftingImage(BaseTest):
    def setUp(self):
        super().setUp()
        self.shift_img_page = ShiftingImagePage(self.driver)

    def testImage(self):
        #Record first location of image then refresh page
        location1 = self.shift_img_page.getLocation(ShiftingImageLocators.Image)
        self.driver.refresh()

        #Record second location of image and verify the image shifted on the x axis
        location2 = self.shift_img_page.getLocation(ShiftingImageLocators.Image)
        self.assertNotEqual(location1['x'], location2['x'])

if __name__ == "__main__":
    unittest.main()