@echo off
chcp 65001 > nul
echo Running SauceDemo tests...

if not exist venv\Scripts\activate.bat (
    echo ERROR: Run install.bat first!
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
pytest tests/test_login.py -v
pause