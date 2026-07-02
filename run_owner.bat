@echo off
title HestiaStay Owner Suite

echo.
echo ======================================
echo Running Owner Suite
echo ======================================
echo.

python -m pytest -m owner -v -s ^
--html=reports/owner_report.html ^
--self-contained-html

echo.
echo Owner Suite Completed
pause