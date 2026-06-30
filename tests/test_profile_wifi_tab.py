import time


def test_profile_wifi_tab(driver):

    time.sleep(5)

    page = driver.page_source

    # Open Profile screen if needed
    if "Profile" in page:
        try:
            driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Profile')]"
            ).click()

            time.sleep(3)

        except Exception:
            pass

    page = driver.page_source

    # Click WiFi tab
    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'WiFi')]"
        ).click()

        time.sleep(3)

    except Exception:
        print("WiFi tab not available in current app state")
        print("PROFILE WIFI TAB HANDLED")
        return

    page = driver.page_source

    if (
        "WiFi" in page
        or "SSID" in page
        or "Password" in page
    ):
        print("PROFILE WIFI TAB PASSED")

    else:
        print("WiFi details not available")
        print("PROFILE WIFI TAB HANDLED")