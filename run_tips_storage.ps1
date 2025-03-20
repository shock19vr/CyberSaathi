# CyberSaathi CISO Tips Storage PowerShell Script

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "CyberSaathi CISO Tips Storage" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check if a file name was provided as an argument
if ($args.Count -eq 0) {
    Write-Host "No input file specified." -ForegroundColor Red
    Write-Host "Usage: .\run_tips_storage.ps1 FILENAME.md" -ForegroundColor Yellow
    exit 1
}

$inputFile = $args[0]

# Check if the file exists
if (-not (Test-Path $inputFile)) {
    Write-Host "File not found: $inputFile" -ForegroundColor Red
    exit 1
}

# Run the store_tips.py script with the provided file
Write-Host "Processing file: $inputFile" -ForegroundColor Green
python store_tips.py --input "$inputFile"

Write-Host ""
if ($LASTEXITCODE -eq 0) {
    Write-Host "===================================" -ForegroundColor Green
    Write-Host "Tips successfully stored in MongoDB" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Green
} else {
    Write-Host "===================================" -ForegroundColor Red
    Write-Host "Error storing tips in MongoDB" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
}

Write-Host "" 