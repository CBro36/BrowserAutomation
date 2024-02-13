import unittest
from Tests.base_test import BaseTest
from Pages.dynamic_content_page import DyanmicContentPage
from Resources.locators import DynamicContentLocators

class TestDynamicContent(BaseTest):
    def setUp(self):
        super().setUp()
        self.dynamic_content_page = DyanmicContentPage(self.driver)
    
    """The images and text blocks displayed on the page are randomly chosen, but the number
    of different outcomes is fairly small, which causes these tests to sometimes fail."""
    def testDynamicImage(self):
        #Verifies that the image source is different after a page reload
        prevSrc = self.dynamic_content_page.getAttribute(DynamicContentLocators.Image, "src")
        self.driver.refresh()
        self.assertNotEqual(prevSrc, self.dynamic_content_page.getAttribute(DynamicContentLocators.Image, "src"))

    def testDynamicText(self):
        #Verifies that the text block is different after a page reload
        prevText = self.dynamic_content_page.getText(DynamicContentLocators.Text)
        self.driver.refresh()
        self.assertNotEqual(prevText, self.dynamic_content_page.getText(DynamicContentLocators.Text))

if __name__ == "__main__":
    unittest.main()