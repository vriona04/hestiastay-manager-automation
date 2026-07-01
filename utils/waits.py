import time
from selenium.webdriver.support.ui import WebDriverWait


def small_wait():
    time.sleep(2)


def medium_wait():
    time.sleep(3)


def long_wait():
    time.sleep(5)


def wait_for_text(driver, text, timeout=15):
    return WebDriverWait(driver, timeout).until(
        lambda d: text in d.page_source
    )


def wait_for_any_text(driver, texts, timeout=15):
    return WebDriverWait(driver, timeout).until(
        lambda d: any(text in d.page_source for text in texts)
    )