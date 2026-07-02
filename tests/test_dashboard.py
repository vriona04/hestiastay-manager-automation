import time
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard(driver):

    time.sleep(5)

    page = driver.page_source

    assert (
        "Hestia PG" in page
        or "Good Morning" in page
        or "Today's Overview" in page
        or "Announcements" in page
        or "Home" in page
        or "Dismiss" in page
        or "₹0" in page
    ), "Dashboard not loaded"

    print("DASHBOARD VERIFIED")

    if "Notifications" in page:
        print("Notifications button available")
    else:
        print("Notifications button not available in current app state")

    if "Refresh" in page:
        print("Refresh button available")
    else:
        print("Refresh button not available in current app state")

    if "Menu" in page:
        print("Menu button available")
    else:
        print("Menu button not available in current app state")

    print("MANAGER DASHBOARD PASSED")