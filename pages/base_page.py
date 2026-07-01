from appium.webdriver.common.appiumby import AppiumBy

from utils.logger import log
from utils.navigation_helper import save_xml
from utils.screenshot import save_screenshot
from utils.waits import medium_wait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_by_accessibility_id(self, text):
        try:
            self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                text
            ).click()

            medium_wait()
            log(f"Clicked: {text}")
            return True

        except Exception as e:
            log(f"Unable to click '{text}': {e}")
            return False

    def page_contains(self, text):
        return text in self.driver.page_source

    def save_page_xml(self, filename):
        save_xml(self.driver, filename)

    def take_screenshot(self, filename):
        save_screenshot(self.driver, filename)

    def current_page(self):
        return self.driver.page_source