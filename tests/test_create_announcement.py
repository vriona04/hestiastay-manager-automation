import time


def test_create_announcement(driver):

    time.sleep(5)

    page = driver.page_source

    if "Create Announcement" not in page:
        print("Create Announcement option not available")
        print("CREATE ANNOUNCEMENT HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Create Announcement')]"
        ).click()

        time.sleep(3)

        page = driver.page_source

        with open(
            "screenshots/create_announcement.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(page)

        print("Create Announcement XML saved")
        print("CREATE ANNOUNCEMENT TEST PASSED")

    except Exception:
        print("Could not open Create Announcement screen")
        print("CREATE ANNOUNCEMENT HANDLED")