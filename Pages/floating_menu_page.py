from Pages.base_page import BasePage

class FloatingMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/floating_menu')