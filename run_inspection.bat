@echo off
title HestiaStay Inspection Suite

echo.
echo ======================================
echo Running Inspection Suite
echo ======================================
echo.

python -m pytest -m inspection -v -s ^
--html=reports/inspection_report.html ^
--self-contained-html

echo.
echo Inspection Suite Completed
pause@echo off
title HestiaStay Inspection Suite

echo.
echo ======================================
echo Running Inspection Suite
echo ======================================
echo.

python -m pytest -m inspection -v -s ^
--html=reports/inspection_report.html ^
--self-contained-html

echo.
echo Inspection Suite Completed
pause