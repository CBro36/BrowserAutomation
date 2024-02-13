import unittest
from Tests.base_test import BaseTest
from Pages.nested_frames_page import NestedFramesPage
from Resources.locators import NestedFramesLocators

class TestNestedFrames(BaseTest):
    def setUp(self):
        super().setUp()
        self.nest_frame_page = NestedFramesPage(self.driver)

    def testNestedFrames(self):
        #Switch to top left frame and verify the correct element is accessible
        self.nest_frame_page.switchFrame('frame-top')
        self.nest_frame_page.switchFrame('frame-left')
        self.assertEqual(self.nest_frame_page.getText(NestedFramesLocators.Left), 'LEFT')

        #Switch to top middle frame and verify the correct element is accessible
        self.nest_frame_page.switchFrame('parent')
        self.nest_frame_page.switchFrame('frame-middle')
        self.assertEqual(self.nest_frame_page.getText(NestedFramesLocators.Middle), 'MIDDLE')

        #Switch to top right frame and verify the correct element is accessible
        self.nest_frame_page.switchFrame('parent')
        self.nest_frame_page.switchFrame('frame-right')
        self.assertEqual(self.nest_frame_page.getText(NestedFramesLocators.Right), 'RIGHT')

        #Switch to bottom frame and verify the correct element is accessible
        self.nest_frame_page.switchFrame('default')
        self.nest_frame_page.switchFrame('frame-bottom')
        self.assertEqual(self.nest_frame_page.getText(NestedFramesLocators.Bottom), 'BOTTOM')

if __name__ == "__main__":
    unittest.main()