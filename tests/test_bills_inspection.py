import pytest
import time


@pytest.mark.inspection
def test_bills_inspection(driver):

    time.sleep(5)

    page = driver.page_source

    if "Bills" not in page:
        print("Bills option not available")
        print("BILLS INSPECTION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Bills')]"
        ).click()

        time.sleep(3)

    except Exception:
        print("Bills option not clickable")
        print("BILLS INSPECTION HANDLED")
        return

    page = driver.page_source

    with open(
        "screenshots/bills_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("BILLS XML SAVED")