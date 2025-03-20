@echo off
echo ===================================
echo CyberSaathi Unified Pipeline
echo ===================================
echo.

rem Check for input file parameter
if "%~1"=="" (
    echo Error: No input file specified.
    echo Usage: cybersaathi_main.bat ^<articles_file.md^> [options]
    echo.
    echo Options:
    echo   --skip-summaries     Skip the article summarization step
    echo   --summary-file FILE  Use an existing summary file
    echo   --skip-checks        Skip dependency checks
    exit /b 1
)

rem Process command line arguments
set INPUT_FILE=%~1
set EXTRA_ARGS=

rem Get extra arguments (starting from position 2)
shift
:parse_args
if "%~1"=="" goto run_script
set EXTRA_ARGS=%EXTRA_ARGS% %~1
shift
goto parse_args

:run_script
rem Run the cybersaathi_main.py script with the input file and any extra arguments
echo Running CyberSaathi unified pipeline...
python cybersaathi_main.py --input "%INPUT_FILE%" %EXTRA_ARGS%

if %ERRORLEVEL% neq 0 (
    echo.
    echo ===================================
    echo Error: Pipeline execution failed
    echo ===================================
    exit /b 1
)

exit /b 0 