import unittest
from Tests.base_test import BaseTest
from Pages.file_download_page import FileDownloadPage
from Resources.locators import FileDownloadLocators
from pathlib import Path
import time

class TestFileDownload(BaseTest):
    def setUp(self):
        super().setUp()
        self.file_dl_page = FileDownloadPage(self.driver)
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
    
    def testDownload(self):
        '''Not only were some of the download links not working when I tried them, 
        but the ones showed on the page were inconsistent when I would sometimes 
        reload the page.'''
        
        #Download 3 files
        self.file_dl_page.click(FileDownloadLocators.File1)
        self.file_dl_page.click(FileDownloadLocators.File2)
        self.file_dl_page.click(FileDownloadLocators.File3)
        time.sleep(2)
        
        #Verify that the 3 files downloaded successfully
        self.assertEqual(self.countDir(), 3)

        self.cleanDir()

if __name__ == "__main__":
    unittest.main()