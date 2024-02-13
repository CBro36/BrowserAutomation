import unittest
from Tests.base_test import BaseTest
from Pages.slow_resources_page import SlowResourcesPage

class TestSlowResources(BaseTest):
    def setUp(self, driverType='wire'):
        super().setUp(driverType)
        self.slow_resources_page = SlowResourcesPage(self.driver)

    def testSlowResources(self):
        #Wait for rogue request to finish and print its information
        req = self.driver.wait_for_request('https://the-internet.herokuapp.com/slow_external', 50)
        print(req.url, req.response.status_code, req.response.headers)

if __name__ == "__main__":
    unittest.main()