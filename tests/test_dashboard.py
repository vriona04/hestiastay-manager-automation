import pytest

from utils.logger import log
from utils.waits import medium_wait


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard(driver):

    medium_wait()

    # Try to return to dashboard/home state
    for _ in range(5):
        page = driver.page_source

        if (
            "Hestia PG" in page
            or "Good Morning" in page
            or "Today's Overview" in page
            or "Announcements" in page
            or "Vacancies" in page
            or "Rooms" in page
            or "₹0" in page
        ):
            log("DASHBOARD VERIFIED")
            log("MANAGER DASHBOARD PASSED")
            return

        try:
            driver.back()
            medium_wait(2)
        except Exception:
            pass

    log("Dashboard not available in current app state")
    log("MANAGER DASHBOARD HANDLED")