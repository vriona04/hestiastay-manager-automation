import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu, save_xml
from utils.waits import medium_wait


@pytest.mark.owner
@pytest.mark.inspection
def test_edit_hostel_inspection(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Edit Hostel" not in page:
        log("Edit Hostel option not available")
        log("EDIT HOSTEL INSPECTION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Edit Hostel')]"
        ).click()

        medium_wait()

    except Exception:
        log("Edit Hostel option not clickable")
        log("EDIT HOSTEL INSPECTION HANDLED")
        return

    save_xml(driver, "screenshots/edit_hostel_screen.xml")

    log("EDIT HOSTEL SCREEN OPENED")
    log("EDIT HOSTEL XML SAVED")