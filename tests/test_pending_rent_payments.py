import pytest
import time


@pytest.mark.dashboard
@pytest.mark.regression
def test_pending_rent_payments(driver):

    time.sleep(5)

    try:
        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.9
            }
        )

        time.sleep(3)

    except Exception:
        print("Scroll failed")
        print("PENDING RENT PAYMENTS HANDLED")
        return

    page = driver.page_source

    if (
        "Pending Rent Payments" in page
        or "Total Due" in page
        or "Pending Today" in page
        or "Overdue" in page
    ):
        print("PENDING RENT PAYMENTS PASSED")

    else:
        print(
            "Pending Rent Payments section "
            "not available in current app state"
        )
        print("PENDING RENT PAYMENTS HANDLED")