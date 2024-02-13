import unittest
from Tests.base_test import BaseTest
from Pages.infinite_scroll_page import InfiniteScrollPage

class TestInfiniteScroll(BaseTest):
    def setUp(self):
        super().setUp()
        self.inf_scroll_page = InfiniteScrollPage(self.driver)

    def testScroll(self):
        #Get initial cout of paragraph segements
        count = self.inf_scroll_page.countSegments()
        #In the loop, scroll to the bottom of the page, then verify that the number of paragraph
        #segements is equal to the current count + 1, then update the count
        for i in range(10):
            self.inf_scroll_page.scrollToBottom()
            self.assertEqual(self.inf_scroll_page.countSegments(), count + 1)
            count += 1

if __name__ == "__main__":
    unittest.main()