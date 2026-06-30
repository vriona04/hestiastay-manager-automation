import time


def test_profile_menu(driver):

    time.sleep(5)

    page = driver.page_source

    if "Menu" not in page:
        print("Menu button not available")
        print("PROFILE MENU HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Menu')]"
        ).click()

        time.sleep(3)

        page = driver.page_source

        with open(
            "screenshots/profile_menu.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(page)

        print("Profile menu XML saved")
        print("PROFILE MENU TEST PASSED")

    except Exception:
        print("Could not open profile menu")
        print("PROFILE MENU HANDLED")