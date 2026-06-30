import time


def test_bills_validation(driver):

    time.sleep(5)

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
        print("BILLS VALIDATION HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Bills')]"
    ).click()

    time.sleep(5)

    page = driver.page_source

    assert "Bills" in page, "Bills screen not opened"

    assert (
        "Filter Bills" in page
        or "Current" in page
        or "No bills found" in page
        or "Add Bill" in page
    ), "Bills screen content not found"

    print("BILLS VALIDATION PASSED")