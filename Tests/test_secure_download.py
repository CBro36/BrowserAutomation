import unittest
from Tests.base_test import BaseTest
from Pages.secure_download_page import SecureDownloadPage
from Resources.locators import SecureDownloadLocators
import time
from pathlib import Path

class TestSecureDownload(BaseTest):
    def setUp(self):
        super().setUp(driverType='wire')
        self.secure_dl_page = SecureDownloadPage(self.driver)
        self.directory = Path.cwd() / 'Downloads'

    def countDir(self):
        #Counts the number of files in the Downloads directory
        numFiles = 0

        for f in self.directory.iterdir():
            if f.is_file():
                numFiles += 1

        print(numFiles)
        return numFiles
    
    def cleanDir(self):
        #Gets all files in the Downloads directory and deletes them
        for f in self.directory.iterdir():
            if f.is_file():
                f.unlink()
    
    def testSecureDownload(self):
        #Same as file download after authenticated, download 3 files and verify that they all
        #downloaded successfully
        self.secure_dl_page.click(SecureDownloadLocators.File1)
        self.secure_dl_page.click(SecureDownloadLocators.File2)
        self.secure_dl_page.click(SecureDownloadLocators.File3)
        time.sleep(2)

        self.assertEqual(self.countDir(), 3)

        self.cleanDir()

if __name__ == "__main__":
    unittest.main()