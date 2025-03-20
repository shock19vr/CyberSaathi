@echo off
echo ===================================
echo CyberSaathi - Complete Pipeline
echo ===================================
echo.
echo This will run the complete CyberSaathi pipeline:
echo 1. Web scraper (collect articles)
echo 2. Export to markdown
echo 3. Article summarization
echo 4. CISO tips generation
echo 5. MongoDB storage
echo.

if "%~1"=="" (
    echo Running complete pipeline including scraper...
    python cybersaathi_main.py
) else (
    echo Using provided input file: %~1
    python cybersaathi_main.py %*
)

if %ERRORLEVEL% neq 0 (
    echo.
    echo Error: Pipeline execution failed.
    exit /b 1
)

echo.
echo Pipeline completed successfully!
exit /b 0 