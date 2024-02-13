import unittest
from Tests.base_test import BaseTest
from Pages.javascript_error_page import JavaScriptErrorPage

class TestJavaScriptError(BaseTest):
    def setUp(self):
        super().setUp()
        self.js_error_page = JavaScriptErrorPage(self.driver)

    def testErrorCatching(self):
        errors = self.js_error_page.getLogs()
        
        if errors == []:
            print('No browser errors')
        else:
            print('Browser Errors:')
            print(errors)

if __name__ == "__main__":
    unittest.main()