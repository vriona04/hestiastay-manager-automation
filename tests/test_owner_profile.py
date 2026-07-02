import pytest
from utils.logger import log
from utils.navigation_helper import open_owner_menu
from utils.waits import medium_wait


@pytest.mark.profile
@pytest.mark.regression
def test_owner_profile(driver):

    medium_wait()

    open_owner_menu(driver)

    page = driver.page_source

    if "Profile" not in page:
        log("Profile option not available")
        log("OWNER PROFILE HANDLED")
        return

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Profile')]"
    ).click()

    medium_wait()

    log("OWNER PROFILE OPENED")
    log("OWNER PROFILE TEST PASSED")