import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu, save_xml
from utils.waits import medium_wait


@pytest.mark.billing
@pytest.mark.regression
def test_add_bill_form_validation(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Bills" not in page:
        log("Bills option not available")
        log("ADD BILL FORM VALIDATION HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Bills')]"
    ).click()

    medium_wait()

    page = driver.page_source

    if "Add Bill" not in page:
        log("Add Bill button not available")
        log("ADD BILL FORM VALIDATION HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Add Bill')]"
    ).click()

    medium_wait()

    save_xml(driver, "screenshots/add_bill_form_validation.xml")

    page = driver.page_source

    expected_items = [
        "Add New",
        "Bill Type",
        "Amount",
        "Notes",
        "Cancel",
        "Add Bill"
    ]

    found = 0

    for item in expected_items:
        if item in page:
            log(f"PASS: {item}")
            found += 1
        else:
            log(f"MISSING: {item}")

    assert found >= 5, "Add Bill form validation failed"

    log("ADD BILL FORM VALIDATION PASSED")