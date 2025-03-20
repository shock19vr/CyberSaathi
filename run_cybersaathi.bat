@echo off
echo ===================================
echo CyberSaathi - Cybersecurity Assistant
echo ===================================
echo.

if "%~1"=="" (
    echo Error: No input file specified.
    echo.
    echo Usage: run_cybersaathi.bat ^<articles_file.md^> [options]
    echo.
    echo Options:
    echo   --skip-summaries     Skip the article summarization step
    echo   --summary-file FILE  Use an existing summary file
    echo   --skip-checks        Skip dependency checks
    echo.
    exit /b 1
)

echo Running CyberSaathi pipeline...
echo Input file: %~1
echo.

REM Pass all arguments directly to the Python script
python cybersaathi_main.py %*

if %ERRORLEVEL% neq 0 (
    echo.
    echo Error: Pipeline execution failed.
    exit /b 1
)

echo.
echo Pipeline completed successfully!
exit /b 0 