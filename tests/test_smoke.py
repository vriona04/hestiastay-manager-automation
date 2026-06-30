import time
from pages.navigation_page import NavigationPage


def test_smoke(driver):

    nav = NavigationPage(driver)

    print("Verifying Dashboard")
    nav.go_home()
    time.sleep(2)

    print("Opening Vacancies")
    nav.open_vacancies()
    time.sleep(3)

    print("Opening Rooms")
    nav.open_rooms()
    time.sleep(3)

    print("Opening Booked")
    nav.open_booked()
    time.sleep(3)

    print("Refreshing Dashboard")
    nav.refresh_dashboard()
    time.sleep(3)

    print("MANAGER SMOKE TEST PASSED")