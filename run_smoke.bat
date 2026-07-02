@echo off
title HestiaStay Smoke Suite

echo.
echo ======================================
echo Running Smoke Suite
echo ======================================
echo.

python -m pytest -m smoke -v -s ^
--html=reports/smoke_report.html ^
--self-contained-html

echo.
echo Smoke Suite Completed
pause