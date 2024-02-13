import unittest
from Tests.base_test import BaseTest
from Pages.challenging_dom_page import ChallengingDOMPage
from Resources.locators import ChallengingDOMLocators

class testChallengingDOM(BaseTest):
    def setUp(self):
        super().setUp()
        self.challenging_dom_page = ChallengingDOMPage(self.driver)
    
    def testChallengingDOM(self):
        #Verify that the button's id changes with each click
        prevID = self.challenging_dom_page.getAttribute(ChallengingDOMLocators.Button, "id")
        self.challenging_dom_page.click(ChallengingDOMLocators.Button)
        self.assertNotEqual(prevID, self.challenging_dom_page.getAttribute(ChallengingDOMLocators.Button, "id"))

        #Verify table element includes correct text
        self.assertEqual("Apeirian2", self.challenging_dom_page.getText(ChallengingDOMLocators.TableElement))

        #Verify canvas element displays a random number on each page load
        prevAnswer = self.challenging_dom_page.getCanvasNum(ChallengingDOMLocators.CanvasScript)
        self.driver.refresh()
        self.assertNotEqual(prevAnswer, self.challenging_dom_page.getCanvasNum(ChallengingDOMLocators.CanvasScript))

if __name__ == "__main__":
    unittest.main()