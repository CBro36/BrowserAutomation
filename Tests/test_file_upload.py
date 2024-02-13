import unittest
from Tests.base_test import BaseTest
from Pages.file_upload_page import FileUploadPage
from Resources.locators import FileUploadLocators
from pathlib import Path

class TestFileUpload(BaseTest):
    def setUp(self):
        super().setUp()
        self.file_upload_page = FileUploadPage(self.driver)
        self.file = Path.cwd() / 'Resources' / 'Sample_Files' / 'File upload.docx'

    def testUpload(self):
        #Get file to upload, upload it, verify the file was uploaded successfully
        fileName = str(self.file)
        self.file_upload_page.uploadFile(fileName)
        self.assertEqual(self.file_upload_page.getText(FileUploadLocators.UploadedFile), self.file.name)

if __name__ == "__main__":
    unittest.main()