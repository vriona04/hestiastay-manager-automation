import pytest
import time


@pytest.mark.dashboard
@pytest.mark.inspection
def test_dashboard_scroll_inspection(driver):

    time.sleep(5)

    driver.execute_script(
        "mobile: scrollGesture",
        {
            "left": 100,
            "top": 600,
            "width": 900,
            "height": 1200,
            "direction": "down",
            "percent": 0.9
        }
    )

    time.sleep(3)

    page = driver.page_source

    with open(
        "screenshots/dashboard_scrolled.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("Dashboard scrolled XML saved")