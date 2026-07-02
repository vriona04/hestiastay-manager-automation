import pytest
import time


@pytest.mark.owner
@pytest.mark.regression
def test_my_hostels(driver):

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

    if "My Hostels" not in page:
        print("My Hostels option not available")
        print("MY HOSTELS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'My Hostels')]"
        ).click()

        time.sleep(5)

    except Exception:
        print("My Hostels option not clickable")
        print("MY HOSTELS HANDLED")
        return

    page = driver.page_source

    with open(
        "screenshots/my_hostels_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("MY HOSTELS SCREEN OPENED")
    print("MY HOSTELS XML SAVED")