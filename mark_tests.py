from pathlib import Path

MARKERS = {
    "test_smoke.py": ["smoke", "regression"],

    "test_dashboard.py": ["dashboard", "regression"],
    "test_dashboard_scroll_inspection.py": ["dashboard", "inspection"],
    "test_pending_rent_payments.py": ["dashboard", "regression"],
    "test_guests_vacating.py": ["dashboard", "regression"],
    "test_hostel_statistics.py": ["dashboard", "regression"],

    "test_bills.py": ["billing", "regression"],
    "test_bills_validation.py": ["billing", "regression"],
    "test_credits.py": ["billing", "regression"],
    "test_credits_validation.py": ["billing", "regression"],

    "test_owner_profile.py": ["profile", "regression"],
    "test_owner_contact_information.py": ["profile", "regression"],
    "test_profile_wifi_tab.py": ["profile", "regression"],
    "test_profile_docs_tab.py": ["profile", "regression"],
    "test_profile_payments_tab.py": ["profile", "regression"],

    "test_my_hostels.py": ["owner", "regression"],
    "test_add_hostel.py": ["owner", "regression"],
    "test_kyc_verification.py": ["owner", "regression"],
    "test_earnings.py": ["owner", "regression"],

    "test_bottom_navigation.py": ["navigation", "regression"],

    "test_menu_inspection.py": ["inspection"],
    "test_bills_inspection.py": ["inspection"],
    "test_manager_dashboard_inspection.py": ["inspection"],
}


def add_markers(file_path, markers):
    text = file_path.read_text(encoding="utf-8")

    if "import pytest" not in text:
        text = "import pytest\n" + text

    marker_lines = "\n".join([f"@pytest.mark.{m}" for m in markers])

    if marker_lines in text:
        return

    text = text.replace(
        "def test_",
        marker_lines + "\ndef test_",
        1
    )

    file_path.write_text(text, encoding="utf-8")


for filename, markers in MARKERS.items():
    path = Path("tests") / filename

    if path.exists():
        add_markers(path, markers)
        print(f"Updated: {filename}")
    else:
        print(f"Missing: {filename}")