@echo off

echo ======================================
echo HestiaStay Manager Regression Started
echo ======================================

python -m pytest -v -s ^
tests/test_smoke.py ^
tests/test_dashboard.py ^
tests/test_bottom_navigation.py ^
tests/test_refresh.py ^
tests/test_announcements.py ^
tests/test_booked_rooms.py ^
tests/test_create_announcement.py ^
tests/test_profile_menu.py ^
tests/test_hostel_statistics.py ^
tests/test_pending_rent_payments.py ^
tests/test_guests_vacating.py ^
tests/test_owner_profile.py ^
tests/test_profile_wifi_tab.py ^
tests/test_profile_docs_tab.py ^
tests/test_profile_payments_tab.py ^
tests/test_bills.py ^
tests/test_bills_validation.py ^
tests/test_credits.py ^
tests/test_credits_validation.py ^
tests/test_earnings.py ^
tests/test_kyc_verification.py ^
tests/test_my_hostels.py ^
tests/test_add_hostel.py ^
tests/test_manager_dashboard_inspection.py ^
tests/test_dashboard_scroll_inspection.py ^
tests/test_menu_inspection.py ^
tests/test_bills_inspection.py ^
--html=reports/final_regression.html ^
--self-contained-html

echo.
echo ======================================
echo Regression Execution Completed
echo ======================================

pause