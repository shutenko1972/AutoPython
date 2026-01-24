@echo off
chcp 65001 > nul
echo ========================================
echo   SAUCEDEMO AUTOTESTS - INSTALLER
echo ========================================
echo.

echo [1/4] Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [2/4] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists.
) else (
    python -m venv venv
    echo Virtual environment created.
)

echo [3/4] Activating environment...
call venv\Scripts\activate.bat

echo [4/4] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo INSTALLATION COMPLETE!
echo.
echo To run tests:
echo   1. run_simple.bat    - Basic tests
echo   2. run_allure.bat    - Tests with reports
echo ========================================
pause