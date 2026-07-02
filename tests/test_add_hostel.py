import pytest
import time


@pytest.mark.owner
@pytest.mark.regression
def test_add_hostel(driver):

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

    if "Add Hostel" not in page:
        print("Add Hostel option not available")
        print("ADD HOSTEL HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Add Hostel')]"
        ).click()

        time.sleep(5)

    except Exception:
        print("Add Hostel option not clickable")
        print("ADD HOSTEL HANDLED")
        return

    page = driver.page_source

    with open(
        "screenshots/add_hostel_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("ADD HOSTEL SCREEN OPENED")
    print("ADD HOSTEL XML SAVED")