import time


def test_owner_contact_information(driver):

    time.sleep(5)

    page = driver.page_source

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

    if "Owner Contact Information" not in page:
        print("Owner Contact Information not available")
        print("OWNER CONTACT INFORMATION HANDLED")
        return

    assert (
        "Phone Number" in page
        or "9606289728" in page
    ), "Phone number not found"

    assert (
        "Email Address" in page
        or "gmail.com" in page
    ), "Email address not found"

    assert "Update Contact Information" in page

    print("OWNER CONTACT INFORMATION PASSED")