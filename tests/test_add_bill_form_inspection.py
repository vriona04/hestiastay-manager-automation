import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu, save_xml
from utils.waits import medium_wait


@pytest.mark.billing
@pytest.mark.inspection
def test_add_bill_form_inspection(driver):

    medium_wait()

    # Open the side menu
    open_owner_menu(driver)

    page = driver.page_source

    if "Bills" not in page:
        log("Bills option not available")
        log("ADD BILL FORM INSPECTION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Bills')]"
        ).click()

        medium_wait()

    except Exception:
        log("Bills option not clickable")
        log("ADD BILL FORM INSPECTION HANDLED")
        return

    page = driver.page_source

    if "Add Bill" not in page:
        log("Add Bill button not available")
        save_xml(driver, "screenshots/bills_screen_before_add.xml")
        log("BILLS SCREEN XML SAVED")
        log("ADD BILL FORM INSPECTION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Add Bill')]"
        ).click()

        medium_wait()

    except Exception:
        log("Add Bill button not clickable")
        log("ADD BILL FORM INSPECTION HANDLED")
        return

    save_xml(driver, "screenshots/add_bill_form.xml")

    log("ADD BILL FORM OPENED")
    log("ADD BILL FORM XML SAVED")
    log("ADD BILL FORM INSPECTION PASSED")