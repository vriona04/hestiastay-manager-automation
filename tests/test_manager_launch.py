import time


def test_manager_app_launch(driver):
    time.sleep(5)

    page = driver.page_source

    assert (
        "Login" in page
        or "Sign In" in page
        or "Dashboard" in page
        or "Home" in page
        or "Hestia" in page
    ), "Manager app did not launch properly"

    print("MANAGER APP LAUNCH PASSED")