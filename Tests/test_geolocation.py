import unittest
from Tests.base_test import BaseTest
from Pages.geolocation_page import GeolocationPage
from Resources.locators import GeolocationLocators

class TestGeolocation(BaseTest):
    def setUp(self):
        super().setUp()
        #Sets the webdriver's latitude and longitude to hard coded values to ensure
        #this test works across different machines
        self.lat = 37.2514795
        self.lng = -115.8864098
        self.accuracy = 100
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": self.lat,
            "longitude": self.lng,
            "accuracy": self.accuracy
        })
        self.geo_page = GeolocationPage(self.driver)

    def testGeolocator(self):
        #Click the button and verify the page gives the same values that we set
        self.geo_page.click(GeolocationLocators.Button)
        self.assertEqual(self.geo_page.getText(GeolocationLocators.Latitude), str(self.lat))
        self.assertEqual(self.geo_page.getText(GeolocationLocators.Longitude), str(self.lng))

if __name__ == "__main__":
    unittest.main()