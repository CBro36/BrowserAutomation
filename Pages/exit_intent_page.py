from Pages.base_page import BasePage
import autoit

class ExitIntentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/exit_intent')
        self.driver.maximize_window()

    def hoverOutOfViewportPane(self):
        #Moves the mouse out of the viewport pane and hovers over the close window button
        autoit.mouse_move(140, 480)
        autoit.mouse_move(1250, 40)