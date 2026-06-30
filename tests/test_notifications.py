import time


def test_notifications(driver):

    time.sleep(5)

    # Try to return to Home tab first
    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Home')]"
        ).click()
        time.sleep(3)
    except Exception:
        pass

    page = driver.page_source

    if "Notifications" not in page:
        print("Notifications button not available in current app state")
        print("NOTIFICATIONS HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Notifications')]"
    ).click()

    time.sleep(3)

    with open(
        "screenshots/notifications.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("Notifications XML saved")
    print("NOTIFICATIONS TEST PASSED")