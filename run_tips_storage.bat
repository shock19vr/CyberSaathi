@echo off
echo ===================================
echo CyberSaathi CISO Tips Storage
echo ===================================

REM Check if a file name was provided as an argument
if "%~1"=="" (
    echo No input file specified.
    echo Usage: .\run_tips_storage.bat FILENAME.md
    exit /b 1
)

REM Check if the file exists
if not exist "%~1" (
    echo File not found: %~1
    exit /b 1
)

REM Run the store_tips.py script with the provided file
echo Processing file: %~1
python store_tips.py --input "%~1"

echo.
if %ERRORLEVEL% EQU 0 (
    echo ===================================
    echo Tips successfully stored in MongoDB
    echo ===================================
) else (
    echo ===================================
    echo Error storing tips in MongoDB
    echo ===================================
)

echo. 