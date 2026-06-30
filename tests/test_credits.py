import time


def test_credits(driver):

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

    if "Credits" not in page:
        print("Credits option not available")
        print("CREDITS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Credits')]"
        ).click()

        time.sleep(5)

    except Exception:
        print("Credits option not clickable")
        print("CREDITS HANDLED")
        return

    with open(
        "screenshots/credits_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("CREDITS SCREEN OPENED")
    print("CREDITS XML SAVED")