@echo off
title HestiaStay Billing Suite

echo.
echo ======================================
echo Running Billing Suite
echo ======================================
echo.

python -m pytest -m billing -v -s ^
--html=reports/billing_report.html ^
--self-contained-html

echo.
echo Billing Suite Completed
pause