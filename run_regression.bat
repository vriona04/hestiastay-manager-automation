@echo off

echo ======================================
echo HestiaStay Manager Regression Started
echo ======================================

python -m pytest -v -s ^
tests/test_manager_launch.py ^
tests/test_dashboard.py ^
tests/test_bottom_navigation.py ^
tests/test_refresh.py ^
tests/test_notifications.py ^
tests/test_menu.py ^
tests/test_announcements.py ^
tests/test_vacancies.py ^
tests/test_rooms.py ^
tests/test_booked_rooms.py ^
tests/test_create_announcement.py ^
tests/test_profile_menu.py ^
tests/test_hostel_statistics.py ^
tests/test_smoke.py ^
--html=reports/final_regression.html ^
--self-contained-html

echo.
echo ======================================
echo Regression Execution Completed
echo ======================================

pause