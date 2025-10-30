@echo off
REM LoliCode Generator GUI Launcher Script for Windows

echo ======================================
echo LoliCode Generator GUI Launcher
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed!
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

REM Display Python version
echo Python version:
python --version

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Warning: tkinter is not available!
    echo tkinter should come with Python on Windows.
    echo Please reinstall Python and make sure to check "tcl/tk and IDLE" during installation.
    echo.
    pause
)

REM Check if requirements are installed
echo.
echo Checking dependencies...
python -c "import pytest" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Launching LoliCode Generator GUI...
echo.
python gui_app.py

echo.
echo GUI closed.
pause
