import unittest
from Tests.base_test import BaseTest
from Pages.shadow_dom_page import ShadowDOMPage
from Resources.locators import ShadowDOMLocators

class TestShadowDOM(BaseTest):
    def setUp(self):
        super().setUp()
        self.shadow_dom_page = ShadowDOMPage(self.driver)

    def testShadowDOM(self):
        #Print the text of the shadow host, switch to shadow root, verify shadow root text is accessible
        print(self.shadow_dom_page.getText(ShadowDOMLocators.ShadowHost1))
        shadowRoot = self.shadow_dom_page.switchToShadow(ShadowDOMLocators.ShadowHost1)
        shadowText1 = self.shadow_dom_page.getShadowElem(shadowRoot, ShadowDOMLocators.RealText)
        self.assertIn('My default text', shadowText1)
        print(shadowText1)
        
        #Same test but with list elements in the shadow host
        print(self.shadow_dom_page.getText(ShadowDOMLocators.ListElem1))
        print(self.shadow_dom_page.getText(ShadowDOMLocators.ListElem2))
        shadowRoot = self.shadow_dom_page.switchToShadow(ShadowDOMLocators.Shadowhost2)
        shadowText2 = self.shadow_dom_page.getShadowElem(shadowRoot, ShadowDOMLocators.RealText)
        self.assertIn('My default text', shadowText2)
        print(shadowText2)

if __name__ == "__main__":
    unittest.main()