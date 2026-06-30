import time


def test_menu_inspection(driver):

    time.sleep(5)

    # Tap top-right menu area
    driver.execute_script(
        "mobile: clickGesture",
        {"x": 1000, "y": 180}
    )

    time.sleep(3)

    page = driver.page_source

    with open(
        "screenshots/menu_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("MENU XML SAVED")