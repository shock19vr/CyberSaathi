@echo off
echo ===================================
echo CyberSaathi CISO Tips Processor
echo ===================================
echo.

rem Check for input file parameter
if "%~1"=="" (
    echo Error: No input file specified.
    echo Usage: process_tips.bat ^<article_summaries_file.md^>
    exit /b 1
)

rem Check if the input file exists
if not exist "%~1" (
    echo Error: Input file "%~1" not found.
    exit /b 1
)

set INPUT_SUMMARIES=%~1
set TIMESTAMP=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%
set OUTPUT_TIPS=ciso_tips_%TIMESTAMP%.md

echo [1/2] Generating CISO tips from article summaries...
python ciso_tips_agent.py --input "%INPUT_SUMMARIES%" --output "%OUTPUT_TIPS%"

if %ERRORLEVEL% neq 0 (
    echo Error: Failed to generate CISO tips.
    exit /b 1
)

echo [2/2] Storing tips in MongoDB...
python store_tips.py --input "%OUTPUT_TIPS%"

if %ERRORLEVEL% neq 0 (
    echo Error: Failed to store tips in MongoDB.
    exit /b 1
)

echo.
echo ===================================
echo Process completed successfully!
echo - Tips generated: %OUTPUT_TIPS%
echo - Tips stored in MongoDB
echo ===================================

exit /b 0 