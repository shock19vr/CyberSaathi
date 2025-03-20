# CyberSaathi CISO Tips Processor
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "CyberSaathi CISO Tips Processor" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check for input file parameter
if ($args.Count -eq 0) {
    Write-Host "Error: No input file specified." -ForegroundColor Red
    Write-Host "Usage: .\process_tips.ps1 <article_summaries_file.md>" -ForegroundColor Yellow
    exit 1
}

$inputSummaries = $args[0]

# Check if the input file exists
if (-not (Test-Path $inputSummaries)) {
    Write-Host "Error: Input file '$inputSummaries' not found." -ForegroundColor Red
    exit 1
}

# Generate timestamp for output files
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$outputTips = "ciso_tips_$timestamp.md"

# Step 1: Generate CISO tips
Write-Host "[1/2] Generating CISO tips from article summaries..." -ForegroundColor Cyan
python ciso_tips_agent.py --input "$inputSummaries" --output "$outputTips"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to generate CISO tips." -ForegroundColor Red
    exit 1
}

# Step 2: Store tips in MongoDB
Write-Host "[2/2] Storing tips in MongoDB..." -ForegroundColor Cyan
python store_tips.py --input "$outputTips"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to store tips in MongoDB." -ForegroundColor Red
    exit 1
}

# Success message
Write-Host ""
Write-Host "===================================" -ForegroundColor Green
Write-Host "Process completed successfully!" -ForegroundColor Green
Write-Host "- Tips generated: $outputTips" -ForegroundColor Green
Write-Host "- Tips stored in MongoDB" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Green

exit 0 