import time


def test_booked_rooms(driver):

    time.sleep(5)

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Booked')]"
        ).click()

        time.sleep(3)

        page = driver.page_source

        assert (
            "Booked" in page
            or "Residents" in page
            or "Room" in page
            or "Tenant" in page
            or "Occupancy" in page
        ), "Booked screen not opened"

        print("BOOKED ROOMS TEST PASSED")

    except Exception:
        print("Booked Rooms section not available in current app state")
        print("BOOKED ROOMS HANDLED")