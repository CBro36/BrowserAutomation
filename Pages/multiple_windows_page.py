from Pages.base_page import BasePage

class MultipleWindowsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/windows')

    def switchWindows(self):
        #Switches to newly opened window
        self.driver.switch_to.window(self.driver.window_handles[1])