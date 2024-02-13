import unittest
from Tests.base_test import BaseTest
from Pages.broken_image_page import BrokenImagePage

class testBrokenImage(BaseTest):
    def setUp(self):
        super().setUp()
        self.broken_image_page = BrokenImagePage(self.driver)

    #Checks if an image is broken by checking if its natural width is 0
    def checkImage(self, image):
        width = image.get_attribute("naturalWidth")
        if width != "0":
            return True
        else:
            return False
    
    def testImages(self):
        images = self.broken_image_page.getImages()
        #Check if each image is broken or not
        for img in images:
            if not self.checkImage(img):
                print(img.get_attribute("outerHTML")+ " is broken")

if __name__ == "__main__":
    unittest.main()