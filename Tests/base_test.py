from selenium import webdriver
from seleniumwire import webdriver as wiredriver
import unittest
from pathlib import Path

class BaseTest(unittest.TestCase):
    #Can choose seleniumwire's driver if access to requests is needed
    def setUp(self, driverType='default'):
        if driverType == 'default':
            chrome_options = webdriver.ChromeOptions()
            prefs = {'download.default_directory' : str(Path.cwd() / 'Downloads')}
            chrome_options.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(options=chrome_options)
        elif driverType == 'wire':
            chrome_options = wiredriver.ChromeOptions()
            prefs = {'download.default_directory' : str(Path.cwd() / 'Downloads')}
            chrome_options.add_experimental_option('prefs', prefs)
            self.driver = wiredriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()