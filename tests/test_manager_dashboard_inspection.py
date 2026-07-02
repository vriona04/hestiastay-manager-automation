import pytest
import time


@pytest.mark.inspection
def test_manager_dashboard_inspection(driver):

    time.sleep(8)

    page = driver.page_source

    with open(
        "screenshots/manager_dashboard.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("Manager dashboard XML saved")

    assert True