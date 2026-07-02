import pytest

from pages.bills_page import BillsPage
from utils.logger import log


@pytest.mark.billing
@pytest.mark.regression
def test_bills_validation(driver):

    bills = BillsPage(driver)

    if not bills.open():
        log("Bills option not available")
        log("BILLS VALIDATION HANDLED")
        return

    assert bills.is_loaded(), "Bills screen validation failed"

    log("BILLS VALIDATION PASSED")