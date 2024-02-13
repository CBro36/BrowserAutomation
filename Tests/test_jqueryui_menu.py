import unittest
from Tests.base_test import BaseTest
from Pages.jqueryui_menu_page import JQueryUIMenuPage
from Resources.locators import JQueryUIMenuLocators
from pathlib import Path
import time

class TestJQueryUIMenu(BaseTest):
    def setUp(self):
        super().setUp()
        self.jqui_menu_page = JQueryUIMenuPage(self.driver)
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

    def testDownloads(self):
        #Hover over the first two menu buttons
        self.jqui_menu_page.mouseOver(JQueryUIMenuLocators.EButton)
        self.jqui_menu_page.mouseOver(JQueryUIMenuLocators.Downloads)
        #Click each download link
        self.jqui_menu_page.click(JQueryUIMenuLocators.PDFLink)
        self.jqui_menu_page.click(JQueryUIMenuLocators.CSVLink)
        self.jqui_menu_page.click(JQueryUIMenuLocators.ExcelLink)
        time.sleep(2)

        #Verify each file was downloaded successfully
        self.assertEqual(self.countDir(), 3)
        
        self.cleanDir()

if __name__ == "__main__":
    unittest.main()