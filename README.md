# CyberSaathi - Cybersecurity Assistant

CyberSaathi is an AI-powered cybersecurity assistant that processes security articles, generates summaries, and provides actionable CISO tips for organizations.

## System Components

### Data Collection

- **Scraper.py**: Scrapes cybersecurity articles from news websites
- **export_to_markdown.py**: Exports scraped articles to markdown format

### Article Processing

- **article_summarizer.py**: Summarizes cybersecurity articles from markdown files
- **article_summaries_*.md**: Output files containing article summaries

### CISO Tips System

- **ciso_tips_agent.py**: Generates actionable security tips from articles
- **store_tips.py**: Stores tips in MongoDB for easy retrieval
- **query_tips.py**: Allows querying the tips database by date or article ID
- **run_tips_storage.bat/ps1**: Helper scripts for storing tips (Windows)
- **process_tips.bat/ps1**: Full automation script for generating and storing tips

### Unified Pipeline

- **cybersaathi_main.py**: Combines all functionality in a single workflow:
  1. Web scraping (collects articles)
  2. Export to markdown
  3. Article summarization
  4. CISO tips generation
  5. MongoDB storage
- **run.bat**: Simple script to run the complete pipeline
- **run_cybersaathi.ps1**: PowerShell script to run the complete pipeline

## Detailed Documentation

- [CISO Tips System Documentation](README_TIPS.md)

## Setup Requirements

1. **Python 3.8+**
2. **MongoDB** (local or Atlas)
3. **Ollama** with llama3:8b model
4. **Selenium WebDriver** for web scraping
5. **Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start Guide

### Using the Unified Pipeline

The simplest way to run the entire CyberSaathi workflow:

```bash
# Run the complete pipeline from scraping to storage:
python cybersaathi_main.py

# Or use existing articles file instead of scraping:
python cybersaathi_main.py cybersecurity_articles.md
```

For Windows users (recommended):
```cmd
# Command Prompt (complete pipeline):
run.bat

# Use existing articles file:
run.bat cybersecurity_articles.md

# PowerShell option:
.\run_cybersaathi.ps1
```

Options:
- `--skip-scraper`: Skip the web scraping step (requires input file)
- `--skip-summaries`: Skip the article summarization step
- `--summary-file FILE`: Use an existing summary file instead of generating one
- `--skip-checks`: Skip dependency checks

### Using Individual Components

1. **Scrape articles**:
   ```bash
   python Scraper.py --limit 10
   python export_to_markdown.py --output cybersecurity_articles.md
   ```

2. **Process articles**:
   ```bash
   python article_summarizer.py --input cybersecurity_articles.md
   ```

3. **Generate CISO tips**:
   ```bash
   python ciso_tips_agent.py --input article_summaries.md --output ciso_tips.md
   ```

4. **Store tips in MongoDB**:
   ```bash
   python store_tips.py --input ciso_tips.md
   ```

5. **Query tips**:
   ```bash
   python query_tips.py --list
   python query_tips.py --id article_1
   ```

## Windows Automation

For Windows users, we provide batch and PowerShell scripts to automate workflows:

```powershell
# Using PowerShell
.\run_tips_storage.ps1 ciso_tips.md
.\process_tips.ps1 article_summaries.md

# Using Command Prompt
.\run_tips_storage.bat ciso_tips.md
.\process_tips.bat article_summaries.md
```

See [CISO Tips Documentation](README_TIPS.md) for detailed Windows usage instructions.

## Project Structure

```
CyberSaathi/
├── Scraper.py
├── export_to_markdown.py
├── article_summarizer.py
├── ciso_tips_agent.py
├── store_tips.py
├── query_tips.py
├── cybersaathi_main.py
├── process_tips.bat
├── process_tips.ps1
├── run.bat               <-- Simplest option for complete pipeline
├── run_cybersaathi.ps1   <-- PowerShell option for complete pipeline
├── run_tips_storage.bat
├── run_tips_storage.ps1
├── README.md
├── README_TIPS.md
└── requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 