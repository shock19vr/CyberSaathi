# CyberSaathi - Cybersecurity Assistant
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "CyberSaathi - Complete Pipeline" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This will run the complete CyberSaathi pipeline:" -ForegroundColor Yellow
Write-Host "1. Web scraper (collect articles)"
Write-Host "2. Export to markdown"
Write-Host "3. Article summarization"
Write-Host "4. CISO tips generation"
Write-Host "5. MongoDB storage"
Write-Host ""

if ($args.Count -eq 0) {
    # No arguments, run complete pipeline including scraper
    Write-Host "Running complete pipeline including scraper..." -ForegroundColor Green
    Invoke-Expression "python cybersaathi_main.py"
} else {
    # Validate that input file exists if provided
    $inputFile = $args[0]
    if (-not (Test-Path $inputFile)) {
        Write-Host "Error: Input file '$inputFile' not found." -ForegroundColor Red
        exit 1
    }

    # Run the Python script with all arguments
    Write-Host "Using provided input file: $inputFile" -ForegroundColor Green
    
    # Convert args array to string while preserving quotes
    $argString = ($args | ForEach-Object { 
        if ($_ -match "\s") { 
            """$_""" 
        } else { 
            $_
        }
    }) -join " "
    
    # Execute with direct command
    Invoke-Expression "python cybersaathi_main.py $argString"
}

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Error: Pipeline execution failed." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Pipeline completed successfully!" -ForegroundColor Green
exit 0 