import unittest
from Tests.base_test import BaseTest
from Pages.disappearing_elements_page import DisappearingElementsPage
from Resources.locators import DisappearingElementsLocators

class TestDisappearingElements(BaseTest):
    def setUp(self):
        super().setUp()
        self.dis_elem_page = DisappearingElementsPage(self.driver)

    def testElement(self):
        found = False

        #Keep checking and refreshing for the gallery button until it's visible
        while not found:
            found = self.dis_elem_page.checkVisiblity(DisappearingElementsLocators.GalleryButton)
            if not found:
                self.driver.refresh()

if __name__ == "__main__":
    unittest.main()