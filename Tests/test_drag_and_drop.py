import unittest
from Tests.base_test import BaseTest
from Pages.drag_and_drop_page import DragAndDropPage
from Resources.locators import DragAndDropLocators

class TestDragAndDrop(BaseTest):
    def setUp(self):
        super().setUp()
        self.drag_n_drop_page = DragAndDropPage(self.driver)

    def testDND(self):
        #Verify the boxes are in the expected positions after drag and drop actions
        self.drag_n_drop_page.dnd(DragAndDropLocators.aColumn, DragAndDropLocators.bColumn)
        self.assertEqual(self.drag_n_drop_page.getText(DragAndDropLocators.aColumn), 'B')
        self.assertEqual(self.drag_n_drop_page.getText(DragAndDropLocators.bColumn), 'A')
        
        self.drag_n_drop_page.dnd(DragAndDropLocators.bColumn, DragAndDropLocators.aColumn)
        self.assertEqual(self.drag_n_drop_page.getText(DragAndDropLocators.aColumn), 'A')
        self.assertEqual(self.drag_n_drop_page.getText(DragAndDropLocators.bColumn), 'B')

if __name__ == "__main__":
    unittest.main()