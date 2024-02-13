from Pages.base_page import BasePage
from Resources.locators import HorizontalSliderLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class HorizontalSliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://the-internet.herokuapp.com/horizontal_slider')

    """Credit to James m for this algorithm:
    https://sqa.stackexchange.com/questions/32318/how-to-move-the-slider-at-specific-position-in-selenium
    Calculates the number of pixels needed to move the slider using minimum and maximum values 
    of the slider as well as the width (or height for vertical sliders) of the slider in pixels"""
    def calcPixels(self, amt, smax, smin):
        slider = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(HorizontalSliderLocators.Slider))
        temp = slider.size['width']
        temp = temp / (smax - smin)
        temp = temp * (amt - smin)
        return int(temp), slider
    
    def dragSlider(self, amt, smax, smin):
        #An extension of the pixel calculation algorithm that uses action chains to drag
        #the slider to the correct value
        pixels, slider = self.calcPixels(amt, smax, smin)
        self.actionChains.click_and_hold(slider).move_by_offset(-(int(slider.size['width'] / 2)), 0).move_by_offset(pixels, 0).release().perform()

    def useArrowKeys(self, direction, steps):
        #Uses arrow key input on the slider elemtent depending on the direction passed to the method
        slider = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(HorizontalSliderLocators.Slider))

        if direction == 'right':
            for i in range(steps):
                slider.send_keys(Keys.ARROW_RIGHT)
        elif direction == 'left':
            for i in range(steps):
                slider.send_keys(Keys.ARROW_LEFT)
        else:
            print("Direction must be right or left")