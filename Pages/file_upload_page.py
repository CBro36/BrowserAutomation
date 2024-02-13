from Pages.base_page import BasePage
from Resources.locators import FileUploadLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FileUploadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/upload')

    def uploadFile(self, fn):
        #Send file name to upload field, then click upload button
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(FileUploadLocators.ChooseFile)).send_keys(fn)
        self.click(FileUploadLocators.UploadButton)