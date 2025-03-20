# Cybersecurity News Scraper

A Python application that scrapes cybersecurity news articles from multiple sources and stores them in a MongoDB database. The scraper extracts article titles, dates, content, and URLs, and encrypts sensitive information.

## Features

- Scrapes articles from multiple cybersecurity news sources:
  - The Hacker News
  - Cyber News
- Stores articles in MongoDB with deduplication based on:
  - Article ID (hash of the title)
  - Normalized title content (for intelligent duplicate detection)
- Encrypts article titles using Fernet symmetric encryption
- Generates unique article IDs based on title content
- Command-line interface for customizing scraping behavior

## Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB server running on localhost (default port 27017)
- Chrome or Chromium browser (for Selenium WebDriver)
- ChromeDriver compatible with your Chrome/Chromium version

### Setup

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running on localhost:
   ```
   # On Windows
   net start MongoDB
   
   # On macOS
   brew services start mongodb-community
   
   # On Linux
   sudo systemctl start mongod
   ```

## Usage

Run the scraper using the following command:

```
python Scraper.py [options]
```

### Command-line options

- `--limit N`: Maximum number of articles to scrape from each site (default: 10)
- `--sites [site1 site2 ...]`: Sites to scrape. Options: hackernews, cybernews, all (default: all)

Examples:

```
# Scrape 5 articles from all supported news sites
python Scraper.py --limit 5

# Scrape only from The Hacker News
python Scraper.py --sites hackernews

# Scrape 20 articles from The Hacker News and Cyber News
python Scraper.py --limit 20 --sites hackernews cybernews
```

## MongoDB Integration

The scraper stores articles in a MongoDB database named "scapper" with the following collections:
- `hackernews`: Articles from The Hacker News
- `cybernews`: Articles from Cyber News

Each article document contains:
- `_id`: Unique ID generated from the article title (SHA-256 hash)
- `title`: Original article title
- `encrypted_title`: Encrypted version of the article title
- `url`: Article URL
- `date`: Publication date
- `tags`: Article tags (if available)
- `description`: Full article content
- `source`: Source website (hackernews or cybernews)
- `scraped_at`: Timestamp when the article was scraped

### Deduplication System

The scraper implements a two-level deduplication system:
1. **ID-based deduplication**: Prevents adding articles with the same title hash (ID)
2. **Normalized title deduplication**: Prevents adding articles with similar titles after normalization

This ensures that the database contains only unique articles, even across multiple scraping sessions.

### Accessing the MongoDB Data

You can query the MongoDB database using the MongoDB shell or any MongoDB client:

```
# Connect to MongoDB shell
mongo

# Select the database
use scapper

# Query articles from The Hacker News
db.hackernews.find()

# Find articles with specific words in the title
db.hackernews.find({title: /vulnerability/i})

# Count articles from Cyber News
db.cybernews.countDocuments()
```

## Encryption

The scraper encrypts article titles using Fernet symmetric encryption with a key derived from PBKDF2. The encrypted titles are stored in MongoDB along with other article data.

To decrypt an encrypted title programmatically:

```python
from Scraper import decrypt_text, generate_encryption_key

# Generate the same encryption key used for encryption
key = generate_encryption_key(None)

# Decrypt the encrypted title
decrypted_title = decrypt_text(encrypted_title, key)
print(decrypted_title)
```

## Utility Scripts

The project includes utility scripts:

- **query_articles.py**: Query and view articles from the database with features:
  - Decrypt encrypted titles for verification
  - Search for articles by keywords in title or description
  - Export results to CSV files for analysis
  - Filter by specific collections (news sources)

- **export_to_markdown.py**: Export articles to a well-formatted Markdown file:
  - Export all articles or specific collections
  - Include article metadata (title, date, source, URL)
  - Include full article content
  - Option to include decrypted titles
  - Creates a single Markdown file that can be fed to AI agents

### Using the Query Tool

The query tool provides flexible ways to search and export your article database:

```bash
# Basic usage - view latest 10 articles
python query_articles.py

# View only articles from The Hacker News
python query_articles.py --collection hackernews

# Show articles with decrypted titles
python query_articles.py --decrypt

# Display up to 20 articles
python query_articles.py --limit 20

# Search for articles containing specific text in title or description
python query_articles.py --search "vulnerability"

# Export results to CSV files (creates timestamped files for each collection)
python query_articles.py --export cybersecurity_articles

# List available collections and document counts
python query_articles.py --list

# Combine multiple options
python query_articles.py --collection cybernews --limit 5 --decrypt --search "ransomware" --export ransomware_report
```

### Using the Export to Markdown Tool

The export tool creates a well-formatted Markdown file from your scraped articles:

```bash
# Basic usage - export all articles
python export_to_markdown.py

# Export only articles from a specific source
python export_to_markdown.py --collection hackernews

# Export with a custom filename
python export_to_markdown.py --output cybersecurity_report.md

# Export only 5 articles per collection
python export_to_markdown.py --limit 5

# Include decrypted titles in the output
python export_to_markdown.py --decrypt

# Combine multiple options
python export_to_markdown.py --collection cybernews --limit 10 --output latest_cyber_news.md --decrypt
```

## Troubleshooting

- **WebDriver issues**: Ensure you have the correct ChromeDriver version for your Chrome browser.
- **MongoDB connection errors**: Verify MongoDB is running on localhost port 27017.
- **Memory errors**: Decrease the `--limit` parameter if you encounter memory issues.
- **Slow scraping**: The script includes throttling to avoid overloading websites; this is normal.

## License

[MIT License](LICENSE)

## Disclaimer

This tool is for educational and research purposes only. Always respect website terms of service and robots.txt directives when scraping. Use responsibly. 