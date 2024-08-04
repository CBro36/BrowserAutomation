import unittest
from Tests.base_test import BaseTest
from Pages.wysiwyg_editor_page import WYSIWYGEditorPage
from Resources.locators import WYSIWYGEditorLocators

class TestWYSIWYGEditor(BaseTest):
    def setUp(self):
        super().setUp()
        self.wysiwyg_editor_page = WYSIWYGEditorPage(self.driver)

    def testEditor(self):
        #Warning: The site admins are using the free plan for the
        #TinyMCE editor which has a limited number of editor loads
        #per month. If this limit is exceeded the editor will be
        #read-only and this test will fail.

        #Clear existing text in editor and send text to editor
        self.wysiwyg_editor_page.switchToEditor()
        self.wysiwyg_editor_page.clearText()
        self.wysiwyg_editor_page.sendText('example ')

        #Test ident button, test bold text button
        self.driver.switch_to.default_content()
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Indent)
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Bold)
        self.wysiwyg_editor_page.switchToEditor()
        self.wysiwyg_editor_page.sendText('bold ')
        self.driver.switch_to.default_content()
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Bold)
        
        #Test italics button
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Italics)
        self.wysiwyg_editor_page.switchToEditor()
        self.wysiwyg_editor_page.sendText('italics ')
        self.driver.switch_to.default_content()
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Italics)
        
        #Test undo and redo buttons
        self.wysiwyg_editor_page.switchToEditor()
        self.wysiwyg_editor_page.sendText('undo/redo')
        self.driver.switch_to.default_content()
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Undo)
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Redo)

        #Test alignment button and the formats menu
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.AlignCenter)
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Formats)
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Headings)
        self.wysiwyg_editor_page.click(WYSIWYGEditorLocators.Heading2)

if __name__ == "__main__":
    unittest.main()