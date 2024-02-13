from Pages.base_page import BasePage

class TyposPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/typos')

    def getWords(self, locator=None, text=None):
        #Takes strings of text and splits them by individual words and returns the list of words
        wordList = []
        if locator is not None:
            lines = self.getText(locator).splitlines()
        else:
            lines = text.splitlines()
        
        for line in lines:
            words = line.split()
            for word in words:
                wordList.append(word.strip())

        return wordList