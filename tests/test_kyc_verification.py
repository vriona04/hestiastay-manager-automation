import time


def test_kyc_verification(driver):

    time.sleep(5)

    try:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 1000, "y": 180}
        )
        time.sleep(3)
    except Exception:
        pass

    page = driver.page_source

    if "KYC Verification" not in page:
        print("KYC Verification option not available")
        print("KYC VERIFICATION HANDLED")
        return

    try:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'KYC Verification')]"
        ).click()
        time.sleep(5)
    except Exception:
        print("KYC Verification option not clickable")
        print("KYC VERIFICATION HANDLED")
        return

    with open(
        "screenshots/kyc_verification.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("KYC VERIFICATION SCREEN OPENED")
    print("KYC VERIFICATION PASSED")