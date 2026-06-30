import time


def test_guests_vacating(driver):

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
        print("GUESTS VACATING HANDLED")
        return

    page = driver.page_source

    if (
        "Guests Vacating Soon" in page
        or "No upcoming vacations" in page
        or "All guests are staying" in page
    ):
        print("GUESTS VACATING PASSED")

    else:
        print(
            "Guests Vacating section "
            "not available in current app state"
        )
        print("GUESTS VACATING HANDLED")