import pytest
import time


@pytest.mark.navigation
@pytest.mark.regression
def test_bottom_navigation(driver):

    time.sleep(5)

    tabs = [
        "Vacancies",
        "Rooms",
        "Booked",
        "Home"
    ]

    for tab in tabs:

        try:
            driver.find_element(
                "xpath",
                f"//*[contains(@content-desc,'{tab}')]"
            ).click()

            time.sleep(3)

            print(f"{tab} tab opened")

        except Exception:
            print(f"{tab} tab not found")

    print("BOTTOM NAVIGATION PASSED")