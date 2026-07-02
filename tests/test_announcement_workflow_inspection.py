import os
import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu
from utils.waits import medium_wait


@pytest.mark.owner
@pytest.mark.inspection
def test_announcement_workflow_inspection(driver):

    medium_wait()

    open_owner_menu(driver)

    os.makedirs("screenshots", exist_ok=True)

    with open(
        "screenshots/announcement_workflow.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    log("INITIAL MENU XML SAVED")

    page = driver.page_source

    if "Create Announcement" in page:

        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Create Announcement')]"
        ).click()

        medium_wait()

    elif "Announcements" in page:

        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Announcements')]"
        ).click()

        medium_wait()

    else:

        log("Announcement option not available")
        log("ANNOUNCEMENT WORKFLOW HANDLED")
        return

    with open(
        "screenshots/announcement_workflow.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    log("ANNOUNCEMENT XML SAVED")
    log("ANNOUNCEMENT WORKFLOW PASSED")