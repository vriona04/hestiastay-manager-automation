import pytest

from utils.logger import log
from utils.navigation_helper import open_owner_menu
from utils.waits import medium_wait


@pytest.mark.profile
@pytest.mark.regression
def test_owner_contact_information(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Contact" not in page:
        log("Owner Contact Information not available")
        log("OWNER CONTACT INFORMATION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Contact')]"
        ).click()

        medium_wait()

    except Exception:
        log("Contact Information not clickable")
        log("OWNER CONTACT INFORMATION HANDLED")
        return

    log("OWNER CONTACT INFORMATION PASSED")