from Pages.base_page import BasePage

class DyanmicContentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/dynamic_content?with_content=static')