@echo off
title HestiaStay Profile Suite

echo.
echo ======================================
echo Running Profile Suite
echo ======================================
echo.

python -m pytest -m profile -v -s ^
--html=reports/profile_report.html ^
--self-contained-html

echo.
echo Profile Suite Completed
pause