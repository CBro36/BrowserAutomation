import unittest
from Tests.base_test import BaseTest
from Pages.status_codes_page import StatusCodesPage
from Resources.locators import StatusCodesLocators

class TestStatusCodes(BaseTest):
    def setUp(self, driverType='wire'):
        super().setUp(driverType)
        self.status_codes_page = StatusCodesPage(self.driver)

    def verify(self, expectedURL, expectedSC):
        #Get URL and status code of request and verify they match the expected results
        url, statusCode = self.status_codes_page.getStatusCode()
        self.assertEqual(url, expectedURL)
        self.assertEqual(statusCode, expectedSC)
    
    #Test each status code page
    def testSC200(self):
        self.status_codes_page.click(StatusCodesLocators.Link200)
        self.verify('https://the-internet.herokuapp.com/status_codes/200', 200)

    def testSC301(self):
        self.status_codes_page.click(StatusCodesLocators.Link301)
        self.verify('https://the-internet.herokuapp.com/status_codes/301', 301)

    def testSC404(self):
        self.status_codes_page.click(StatusCodesLocators.Link404)
        self.verify('https://the-internet.herokuapp.com/status_codes/404', 404)

    def testSC500(self):
        self.status_codes_page.click(StatusCodesLocators.Link500)
        self.verify('https://the-internet.herokuapp.com/status_codes/500', 500)
        
if __name__ == "__main__":
    unittest.main()