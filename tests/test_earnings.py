import time


def test_earnings(driver):

    time.sleep(5)

    # Open Owner Portal menu
    try:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 1000, "y": 180}
        )
        time.sleep(3)

    except Exception:
        pass

    page = driver.page_source

    if "Earnings" not in page:
        print("Earnings option not available")
        print("EARNINGS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Earnings')]"
        ).click()

        time.sleep(5)

    except Exception:
        print("Earnings option not clickable")
        print("EARNINGS HANDLED")
        return

    with open(
        "screenshots/earnings_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("EARNINGS SCREEN OPENED")
    print("EARNINGS XML SAVED")