from Pages.base_page import BasePage

class NestedFramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/nested_frames')

    def switchFrame(self, frame):
        """Switches to specified frame
        If 'parent', switches to one frame up in the current hierarchy
        If 'default', switches to the original frame"""
        if frame == "parent":
            self.driver.switch_to.parent_frame()
        elif frame == "default":
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.frame(frame)