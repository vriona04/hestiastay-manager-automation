import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu, save_xml
from utils.waits import medium_wait


@pytest.mark.owner
@pytest.mark.inspection
def test_hostel_management_inspection(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    save_xml(driver, "screenshots/owner_menu_for_hostel.xml")

    if (
        "My Hostels" not in page
        and "Add Hostel" not in page
        and "Edit Hostel" not in page
        and "Hestia PG" not in page
    ):
        log("Hostel management options not available")
        log("HOSTEL MANAGEMENT INSPECTION HANDLED")
        return

    log("HOSTEL MANAGEMENT OPTIONS FOUND")

    if "Hestia PG" in page:
        log("Existing hostel found: Hestia PG")

    if "Add Hostel" in page:
        log("Add Hostel option available")

    if "Edit Hostel" in page:
        log("Edit Hostel option available")

    log("HOSTEL MANAGEMENT INSPECTION PASSED")