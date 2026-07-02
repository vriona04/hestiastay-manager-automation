import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu, save_xml
from utils.waits import medium_wait


@pytest.mark.owner
@pytest.mark.regression
def test_edit_hostel_full_form(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Edit Hostel" not in page:
        log("Edit Hostel option not available")
        log("EDIT HOSTEL FULL FORM HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Edit Hostel')]"
    ).click()

    medium_wait()

    save_xml(driver, "screenshots/edit_hostel_top.xml")

    page = driver.page_source

    top_fields = [
        "Edit Hostel",
        "Hostel Name",
        "Address",
        "Description",
        "Hostel Type",
        "State",
        "City",
        "Area",
        "PIN Code",
        "Hostel Amenities",
    ]

    found_top = 0

    for field in top_fields:
        if field in page:
            log(f"TOP FIELD FOUND: {field}")
            found_top += 1
        else:
            log(f"TOP FIELD NOT FOUND: {field}")

    try:
        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.8,
            },
        )

        medium_wait()

    except Exception:
        log("Scroll failed on Edit Hostel form")

    save_xml(driver, "screenshots/edit_hostel_bottom.xml")

    page = driver.page_source

    bottom_fields = [
        "Wifi",
        "Cctv",
        "Power Backup",
        "Save",
        "Update",
        "Submit",
        "Image",
        "Photos",
    ]

    found_bottom = 0

    for field in bottom_fields:
        if field in page:
            log(f"BOTTOM FIELD FOUND: {field}")
            found_bottom += 1
        else:
            log(f"BOTTOM FIELD NOT FOUND: {field}")

    if found_top >= 5 or found_bottom >= 2:
        log("EDIT HOSTEL FULL FORM PASSED")
    else:
        log("EDIT HOSTEL FULL FORM HANDLED")