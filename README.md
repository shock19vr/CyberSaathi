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

### Unified Pipeline

- **main.py**: Complete unified workflow that combines all functionality:
  1. Web scraping (collects articles)
  2. Export to markdown
  3. Article summarization
  4. CISO tips generation
  5. MongoDB storage

## Detailed Documentation

- [CISO Tips System Documentation](README_TIPS.md)
- [Unified Workflow Documentation](README_UNIFIED.md)

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

The simplest way to run the entire CyberSaathi workflow:

```bash
# Run the complete pipeline from scraping to storage:
python main.py

# Or use existing articles file instead of scraping:
python main.py --skip-scrape --input-file cybersecurity_articles.md
```

Options:
- `--limit N`: Limit the number of articles to scrape (default: 10)
- `--skip-scrape`: Skip the web scraping step (requires input file)
- `--input-file FILE`: Use this markdown file instead of scraping
- `--summary-file FILE`: Use an existing summary file instead of generating one
- `--skip-summaries`: Skip the article summarization step
- `--skip-tips`: Skip the CISO tips generation step
- `--skip-storage`: Skip storing data in MongoDB
- `--verbose`: Show detailed output

### Using Individual Components

If you need to run individual components separately:

1. **Scrape articles**:
   ```bash
   python Scraper.py
   ```

2. **Export from MongoDB to markdown**:
   ```bash
   python export_to_markdown.py --output cybersecurity_articles.md
   ```

3. **Process articles**:
   ```bash
   python article_summarizer.py --input cybersecurity_articles.md
   ```

4. **Generate CISO tips**:
   ```bash
   python ciso_tips_agent.py --input article_summaries.md --output ciso_tips.md
   ```

5. **Store tips in MongoDB**:
   ```bash
   python store_tips.py --input ciso_tips.md
   ```

6. **Query tips**:
   ```bash
   python query_tips.py --list
   python query_tips.py --id article_1
   ```

## Project Structure

```
CyberSaathi/
├── Scraper.py                    # Web scraper for cybersecurity articles
├── export_to_markdown.py         # Exports articles to markdown format
├── article_summarizer.py         # Summarizes articles using Ollama
├── ciso_tips_agent.py            # Generates security tips from articles
├── store_tips.py                 # Stores tips in MongoDB
├── query_tips.py                 # Retrieves tips from MongoDB
├── query_articles.py             # Retrieves articles from MongoDB
├── main.py                       # NEW: Unified workflow script
├── README.md                     # Main documentation
├── README_TIPS.md                # CISO tips system documentation
├── README_UNIFIED.md             # Unified workflow documentation
└── requirements.txt              # Python dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 