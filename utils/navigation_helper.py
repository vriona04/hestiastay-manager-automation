import time


def open_owner_menu(driver):
    try:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 1000, "y": 180}
        )
        time.sleep(3)
        return True
    except Exception:
        return False


def go_back(driver, count=1):
    for _ in range(count):
        try:
            driver.back()
            time.sleep(2)
        except Exception:
            pass


def save_xml(driver, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)


def page_has_any(driver, texts):
    page = driver.page_source
    return any(text in page for text in texts)