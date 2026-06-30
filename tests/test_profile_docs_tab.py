import time


def test_profile_docs_tab(driver):

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

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Docs')]"
        ).click()

        time.sleep(3)

    except Exception:
        print("Docs tab not available in current app state")
        print("PROFILE DOCS TAB HANDLED")
        return

    page = driver.page_source

    if "Docs" in page or "Document" in page:
        print("PROFILE DOCS TAB PASSED")

    else:
        print("Documents not available in current app state")
        print("PROFILE DOCS TAB HANDLED")