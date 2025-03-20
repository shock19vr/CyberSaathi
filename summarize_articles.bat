@echo off
echo ================================
echo Article Summarization Pipeline
echo ================================

echo.
echo Step 1: Export articles from MongoDB to markdown
echo ------------------------------------------------
python export_to_markdown.py --collection all --limit 10
if %ERRORLEVEL% NEQ 0 (
    echo Error exporting articles from MongoDB
    pause
    exit /b 1
)

echo.
echo Step 2: Find the most recent markdown file
echo ------------------------------------------
for /f "tokens=*" %%a in ('dir /b /o-d cybersecurity_articles_*.md') do (
    set LATEST_MD=%%a
    goto found_md
)
:found_md
echo Found markdown file: %LATEST_MD%

echo.
echo Step 3: Generate summaries using Ollama
echo ---------------------------------------
echo Checking if Ollama is running...
curl -s http://localhost:11434/api/tags > nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Ollama is not running! Please start Ollama first.
    echo You can download Ollama from https://ollama.ai/
    pause
    exit /b 1
)

echo Ollama is running, starting summarization...
python article_summarizer.py --input %LATEST_MD%
if %ERRORLEVEL% NEQ 0 (
    echo Error generating summaries
    pause
    exit /b 1
)

echo.
echo Step 4: Find the most recent summary file
echo -----------------------------------------
for /f "tokens=*" %%a in ('dir /b /o-d article_summaries_*.md') do (
    set LATEST_SUMMARY=%%a
    goto found_summary
)
:found_summary
echo Found summary file: %LATEST_SUMMARY%

echo.
echo ================================
echo Pipeline completed successfully!
echo ================================
echo.
echo The summarized articles are available in: %LATEST_SUMMARY%
echo.
pause 