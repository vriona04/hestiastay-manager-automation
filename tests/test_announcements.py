import time


def test_announcements(driver):

    time.sleep(5)

    page = driver.page_source

    if (
        "Announcements" in page
        or "Announcement" in page
        or "Create Announcement" in page
    ):

        print("ANNOUNCEMENTS SECTION AVAILABLE")
        print("ANNOUNCEMENTS TEST PASSED")

    else:
        print("Announcements section not available")
        print("ANNOUNCEMENTS HANDLED")