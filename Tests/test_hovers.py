import unittest
from Tests.base_test import BaseTest
from Pages.hovers_page import HoversPage
from Resources.locators import HoversLocators

class TestHovers(BaseTest):
    def setUp(self):
        super().setUp()
        self.hovers_page = HoversPage(self.driver)

    def processProfile(self, img, caption, link, text):
        #Verifies all of the profile information is initially invisible
        self.assertFalse(self.hovers_page.checkVisiblity(caption))
        self.assertFalse(self.hovers_page.checkVisiblity(link))

        #Hovers over the image and verifies that it's profile information is now visible
        self.hovers_page.mouseOverImg(img)
        self.assertTrue(self.hovers_page.checkVisiblity(caption))
        self.assertTrue(self.hovers_page.checkVisiblity(link))
        self.assertEqual(self.hovers_page.getText(caption), text)

        #Clicks the profile link, since there are no real profiles, it gets a 404 response
        self.hovers_page.click(link)
        self.assertEqual(self.hovers_page.getText(HoversLocators.Message), 'Not Found')

        self.driver.back()
    
    def testHover(self):
        #Process the profile for each image
        self.processProfile(HoversLocators.Image1, HoversLocators.Caption1, HoversLocators.Link1, 'name: user1')
        self.processProfile(HoversLocators.Image2, HoversLocators.Caption2, HoversLocators.Link2, 'name: user2')
        self.processProfile(HoversLocators.Image3, HoversLocators.Caption3, HoversLocators.Link3, 'name: user3')

if __name__ == "__main__":
    unittest.main()