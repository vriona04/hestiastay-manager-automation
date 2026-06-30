import time


def test_bills(driver):

    time.sleep(5)

    # Tap top-right Menu button
    try:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 1000, "y": 180}
        )
        time.sleep(3)
    except Exception:
        pass

    page = driver.page_source

    if "Bills" not in page:
        print("Bills option not available")
        print("BILLS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Bills')]"
        ).click()
        time.sleep(5)
    except Exception:
        print("Bills option not clickable")
        print("BILLS HANDLED")
        return

    with open(
        "screenshots/bills_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("BILLS SCREEN OPENED")
    print("BILLS XML SAVED")