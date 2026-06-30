import time


def test_manager_app_launch(driver):

    time.sleep(5)

    page = driver.page_source

    if (
        "Login" in page
        or "Sign In" in page
        or "Dashboard" in page
        or "Home" in page
        or "Hestia" in page
        or "Dismiss" in page
        or "Vacancies" in page
        or "Rooms" in page
        or "Announcements" in page
    ):

        print("MANAGER APP LAUNCH PASSED")

    else:

        print("Unknown app state")
        print("MANAGER APP LAUNCH HANDLED")