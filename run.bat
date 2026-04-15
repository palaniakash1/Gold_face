@echo off
title Gold Face - Virtual Jewelry Try-On
color 0A

echo ================================================
echo   Gold Face - Virtual Jewelry Try-On
echo ================================================
echo.
echo Choose an option:
echo.
echo   1. Run Webapp (Recommended)
echo   2. Run Desktop App
echo   3. Exit
echo.

set /p choice="Enter choice (1/2/3): "

if "%choice%"=="1" (
    echo.
    echo Starting Webapp...
    echo Opening http://localhost:8000 in your browser...
    cd /d "%~dp0webapp"
    start http://localhost:8000
    python -m http.server 8000
) else if "%choice%"=="2" (
    echo.
    echo Choose desktop version:
    echo   1. Basic (single jewelry)
    echo   2. Enhanced (cycles through combinations)
    echo.
    set /p desktop_choice="Enter choice (1/2): "
    
    cd /d "%~dp0Gold_face"
    
    if "%desktop_choice%"=="1" (
        python main.py
    ) else (
        python new_main.py
    )
) else (
    echo Exiting...
    timeout /t 1 >nul
    exit
)
