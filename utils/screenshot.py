import os


def save_screenshot(driver, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    driver.save_screenshot(file_path)


def save_xml(driver, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)