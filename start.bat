@echo off
REM =====================================================================
REM 💳 SwipeSmart AI — Windows One-Click Startup Script
REM =====================================================================

title SwipeSmart AI Enterprise

cd /d "%~dp0"

echo.
echo =====================================================================
echo   💳  SwipeSmart AI Enterprise  —  Windows Startup
echo =====================================================================
echo.

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    where py >nul 2>nul
    if %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Python was not found on your system!
        echo Please download and install Python 3.10+ from:
        echo   https://www.python.org/downloads/
        echo Make sure to check "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    ) else (
        py run.py %*
        goto finish
    )
)

python run.py %*

:finish
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application exited with code %ERRORLEVEL%.
    pause
)
