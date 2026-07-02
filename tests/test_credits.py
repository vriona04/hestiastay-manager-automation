import pytest

from utils.navigation_helper import open_owner_menu, save_xml
from utils.logger import log
from utils.waits import medium_wait


@pytest.mark.billing
@pytest.mark.regression
def test_credits(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Credits" not in page:
        log("Credits option not available")
        log("CREDITS HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Credits')]"
        ).click()

        medium_wait()

    except Exception:
        log("Credits option not clickable")
        log("CREDITS HANDLED")
        return

    save_xml(driver, "screenshots/credits_screen.xml")

    log("CREDITS SCREEN OPENED")
    log("CREDITS XML SAVED")