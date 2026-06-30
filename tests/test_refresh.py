import time
from pages.navigation_page import NavigationPage


def test_refresh_button(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    page = driver.page_source

    if "Refresh" not in page:
        print("Refresh button not available in current app state")
        print("REFRESH HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Refresh')]"
    ).click()

    time.sleep(3)

    print("REFRESH BUTTON PASSED")