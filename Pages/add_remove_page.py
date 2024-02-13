from Pages.base_page import BasePage

class AddRemovePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/add_remove_elements/')