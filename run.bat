@echo off
title Gold Face - Virtual Jewelry Try-On
color 0A

echo ================================================
echo   Gold Face - Virtual Jewelry Try-On
echo ================================================
echo.
echo Choose an option:
echo.
echo   1. Run Webapp (Recommended - Browser-based)
echo   2. Run Desktop App
echo   0. Exit
echo.

set /p choice="Enter choice (1/2/0): "

if "%choice%"=="1" (
    echo.
    echo Starting Webapp...
    echo Opening http://localhost:8000 in your browser...
    cd /d "%~dp0webapp"
    start http://localhost:8000
    python -m http.server 8000
) else if "%choice%"=="2" (
    echo.
    echo Starting Desktop App...
    cd /d "%~dp0src"
    python main.py
) else (
    echo Exiting...
    timeout /t 1 >nul
    exit
)
