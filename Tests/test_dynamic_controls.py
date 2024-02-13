import unittest
from Tests.base_test import BaseTest
from Pages.dynamic_controls_page import DynamicControlsPage
from Resources.locators import DynamicControlsLocators

class TestDynamicControls(BaseTest):
    def setUp(self):
        super().setUp()
        self.dynamic_controls_page = DynamicControlsPage(self.driver)

    def testAddRemove(self):
        #Click the checkbox, click the remove button, verify that the checkbox disappeared
        self.dynamic_controls_page.click(DynamicControlsLocators.Checkbox1)        
        self.dynamic_controls_page.clickButton(DynamicControlsLocators.AddRemove)
        self.assertFalse(self.dynamic_controls_page.checkVisiblity(DynamicControlsLocators.Checkbox1))
        
        #Click the add button and verify that a new checkbox is visible
        self.dynamic_controls_page.clickButton(DynamicControlsLocators.AddRemove)
        self.assertTrue(self.dynamic_controls_page.checkVisiblity(DynamicControlsLocators.Checkbox2))
        
        #Click checkbox, click the remove button, and verify the new checkbox has disappeared
        self.dynamic_controls_page.click(DynamicControlsLocators.Checkbox2)
        self.dynamic_controls_page.clickButton(DynamicControlsLocators.AddRemove)
        self.assertFalse(self.dynamic_controls_page.checkVisiblity(DynamicControlsLocators.Checkbox2))

    def testEnableDisable(self):
        #Verify text input is disabled
        self.assertFalse(self.dynamic_controls_page.checkTextInput())

        #Click enable button and verify the text input is enabled
        self.dynamic_controls_page.clickButton(DynamicControlsLocators.EnableDisable)
        self.assertTrue(self.dynamic_controls_page.checkTextInput())
        
        #Send text to the input, click disable button, and verify the text input is disabled
        self.dynamic_controls_page.inputText("example")
        self.dynamic_controls_page.clickButton(DynamicControlsLocators.EnableDisable)
        self.assertFalse(self.dynamic_controls_page.checkTextInput())

if __name__ == "__main__":
    unittest.main()