# CyberSaathi Unified Pipeline
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "CyberSaathi Unified Pipeline" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check if at least one argument (input file) is provided
if ($args.Count -eq 0) {
    Write-Host "Error: No input file specified." -ForegroundColor Red
    Write-Host "Usage: .\cybersaathi_main.ps1 <articles_file.md> [options]" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Options:" -ForegroundColor Yellow
    Write-Host "  --skip-summaries     Skip the article summarization step"
    Write-Host "  --summary-file FILE  Use an existing summary file"
    Write-Host "  --skip-checks        Skip dependency checks"
    exit 1
}

# Extract the input file (first argument)
$inputFile = $args[0]

# Extract any additional arguments
$extraArgs = @()
if ($args.Count -gt 1) {
    $extraArgs = $args[1..($args.Count-1)]
}

# Run the cybersaathi_main.py script with the input file and any extra arguments
Write-Host "Running CyberSaathi unified pipeline..." -ForegroundColor Green
$allArgs = @("cybersaathi_main.py", "--input", $inputFile) + $extraArgs
python $allArgs

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "===================================" -ForegroundColor Red
    Write-Host "Error: Pipeline execution failed" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
    exit 1
}

exit 0 