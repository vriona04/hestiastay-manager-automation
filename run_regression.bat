@echo off
title HestiaStay Manager Regression

echo.
echo ======================================
echo HestiaStay Manager Regression Started
echo ======================================
echo.

REM Create folders if they do not exist
if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist screenshots mkdir screenshots

REM Run only Regression Suite
python -m pytest -m regression -v -s ^
--html=reports/final_regression.html ^
--self-contained-html

echo.
echo ======================================
echo Regression Execution Completed
echo ======================================
echo.

pause