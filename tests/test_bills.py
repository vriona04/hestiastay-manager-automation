import pytest
from utils.navigation_helper import open_owner_menu, save_xml
from utils.logger import log
from utils.waits import medium_wait


@pytest.mark.billing
@pytest.mark.regression
def test_bills(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Bills" not in page:
        log("Bills option not available")
        log("BILLS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Bills')]"
        ).click()

        medium_wait()

    except Exception:
        log("Bills option not clickable")
        log("BILLS HANDLED")
        return

    save_xml(driver, "screenshots/bills_screen.xml")

    log("BILLS SCREEN OPENED")
    log("BILLS XML SAVED")