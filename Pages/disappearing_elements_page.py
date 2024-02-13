from Pages.base_page import BasePage

class DisappearingElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/disappearing_elements')

    def checkVisiblity(self, locator):
        #Check if gallery button is visible
        result = super().checkVisiblity(locator)
        if result:
            print("Gallery button appeared")
            return True
        else:
            print("Gallery button not found")
            return False