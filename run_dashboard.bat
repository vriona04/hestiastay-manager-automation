@echo off
title HestiaStay Dashboard Suite

echo.
echo ======================================
echo Running Dashboard Suite
echo ======================================
echo.

python -m pytest -m dashboard -v -s ^
--html=reports/dashboard_report.html ^
--self-contained-html

echo.
echo Dashboard Suite Completed
pause