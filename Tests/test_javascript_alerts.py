import unittest
from Tests.base_test import BaseTest
from Pages.javascript_alerts_page import JavaScriptAlertsPage
from Resources.locators import JavaScriptAlertsLocators

class TestJavaScriptAlerts(BaseTest):
    def setUp(self):
        super().setUp()
        self.js_alerts_page = JavaScriptAlertsPage(self.driver)
    
    def testAlerts(self):
        #Test accepting basic alert
        self.js_alerts_page.click(JavaScriptAlertsLocators.JSAlert)
        self.js_alerts_page.handleBasicAlert()
        self.assertEqual(self.js_alerts_page.getText(JavaScriptAlertsLocators.Result), 'You successfully clicked an alert')

        #Test accepting confirmation alert
        self.js_alerts_page.click(JavaScriptAlertsLocators.JSConfirm)
        self.js_alerts_page.handleConfirmAlert()
        self.assertEqual(self.js_alerts_page.getText(JavaScriptAlertsLocators.Result), 'You clicked: Ok')

        #Test dismissing confirmation alert
        self.js_alerts_page.click(JavaScriptAlertsLocators.JSConfirm)
        self.js_alerts_page.handleConfirmAlert(flag='d')
        self.assertEqual(self.js_alerts_page.getText(JavaScriptAlertsLocators.Result), 'You clicked: Cancel')

        #Test accepting prompt alert
        self.js_alerts_page.click(JavaScriptAlertsLocators.JSPrompt)
        self.js_alerts_page.handlePromptAlert("example")
        self.assertEqual(self.js_alerts_page.getText(JavaScriptAlertsLocators.Result), 'You entered: example')

        #Test dismissing prompt alert
        self.js_alerts_page.click(JavaScriptAlertsLocators.JSPrompt)
        self.js_alerts_page.handlePromptAlert("example", flag='d')
        self.assertEqual(self.js_alerts_page.getText(JavaScriptAlertsLocators.Result), 'You entered: null')

if __name__ == "__main__":
    unittest.main()