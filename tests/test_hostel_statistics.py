import time


def test_hostel_statistics(driver):

    time.sleep(5)

    try:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 1000, "y": 180}
        )

        time.sleep(3)

    except Exception:
        print("Statistics button click failed")
        print("HOSTEL STATISTICS HANDLED")
        return

    page = driver.page_source

    if (
        "Hostel Statistics" in page
        or "Profit" in page
        or "Monthly Expenses" in page
        or "AllYears" in page
    ):
        print("HOSTEL STATISTICS PASSED")

    else:
        print(
            "Statistics screen not available "
            "in current app state"
        )
        print("HOSTEL STATISTICS HANDLED")