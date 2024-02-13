from Pages.base_page import BasePage

class JavaScriptAlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    def handleBasicAlert(self):
        #Accepts basic alert
        alert = self.driver.switch_to.alert
        alert.accept()

    def handleConfirmAlert(self, flag='a'):
        #Accepts or dismisses alert based on flag passed to method
        alert = self.driver.switch_to.alert

        if flag == 'a':
            alert.accept()
        elif flag == 'd':
            alert.dismiss()
        else:
            print("Flag must be 'a' for accept or 'd' for dismiss")

    def handlePromptAlert(self, inputstr, flag='a'):
        #Sends string to alert and accepts or dismisses based on flag
        alert = self.driver.switch_to.alert

        if flag == 'a':
            alert.send_keys(inputstr)
            alert.accept()
        elif flag == 'd':
            alert.dismiss()
        else:
            print("Flag must be 'a' for accept or 'd' for dismiss")