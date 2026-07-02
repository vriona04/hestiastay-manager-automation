import pytest

from pages.navigation_page import NavigationPage
from utils.logger import log
from utils.waits import medium_wait


@pytest.mark.smoke
@pytest.mark.regression
def test_smoke(driver):

    nav = NavigationPage(driver)

    log("========== SMOKE TEST STARTED ==========")

    try:
        log("Step 1 : Go Home")
        nav.go_home()
        medium_wait()

        log("Step 2 : Open Vacancies")
        nav.open_vacancies()
        medium_wait()

        log("Step 3 : Open Rooms")
        nav.open_rooms()
        medium_wait()

        log("Step 4 : Open Booked")
        nav.open_booked()
        medium_wait()

        log("Step 5 : Refresh Dashboard")
        nav.refresh_dashboard()
        medium_wait()

        log("========== SMOKE TEST PASSED ==========")

    except Exception as e:
        log(f"SMOKE TEST FAILED : {e}")
        raise