#!/usr/bin/env python3
"""
Export MongoDB Articles to Markdown File

This script exports all articles from the MongoDB database to a well-formatted
Markdown file that can be used to feed an AI agent.
"""

import os
import sys
import pymongo
from datetime import datetime
import argparse

# Import the encryption utilities from Scraper.py
from Scraper import generate_encryption_key, decrypt_text, setup_mongodb

def connect_to_mongodb():
    """Connect to MongoDB and return client and database objects"""
    try:
        # Use the same connection string as in Scraper.py
        client = pymongo.MongoClient("mongodb+srv://ayushchy012:Chahuta3011@article-db.milce.mongodb.net/")
        db = client["scraper"]  # Fix the typo: "scapper" -> "scraper"
        return client, db
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return None, None

def format_article_to_markdown(article, index):
    """Format a single article as markdown"""
    # Get all article fields with fallbacks for missing data
    title = article.get('title', 'No Title')
    date = article.get('date', 'No Date')
    source = article.get('source', 'Unknown Source')
    url = article.get('url', 'No URL')
    tags = article.get('tags', 'No Tags')
    description = article.get('description', 'No content available')
    article_id = article.get('_id', 'No ID')
    
    # Format as markdown
    markdown = f"""
## {index}. {title}

**Source:** {source}  
**Date:** {date}  
**URL:** {url}  
**ID:** {article_id}  
**Tags:** {tags}

### Content:

{description}

---
"""
    return markdown

def export_to_markdown(collections=None, output_file=None, limit=None, include_encrypted=False, decrypt=False):
    """Export articles from MongoDB to a markdown file"""
    # Connect to MongoDB using the setup function from Scraper.py
    mongo = setup_mongodb()
    if mongo is None:
        print("Failed to connect to MongoDB. Check your connection string.")
        return False
    
    try:
        client = mongo["client"]
        db = mongo["db"]
        
        # Determine which collections to use
        if not collections:
            collections = ["hackernews", "cybernews"]
        elif isinstance(collections, str):
            collections = [collections]
        
        # Generate encryption key if needed
        key = None
        if decrypt:
            key = generate_encryption_key(None)
        
        # Set default output file if none provided
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"cybersecurity_articles_{timestamp}.md"
        
        # Start building the markdown content
        markdown_content = f"# Cybersecurity News Articles\n\n"
        markdown_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown_content += f"Number of collections: {len(collections)}\n\n"
        
        # Initialize article counter
        article_count = 0
        
        # Process each collection
        for collection_name in collections:
            if collection_name in ["hackernews", "cybernews"]:
                collection = mongo[collection_name]
                
                # Get articles with optional limit
                query = collection.find()
                if limit:
                    query = query.limit(limit)
                
                articles = list(query)
                
                if articles:
                    markdown_content += f"## Collection: {collection_name}\n\n"
                    
                    # Process each article
                    for article in articles:
                        article_count += 1
                        article_md = format_article_to_markdown(article, article_count)
                        
                        # Add decrypted title if requested
                        if decrypt and 'encrypted_title' in article:
                            try:
                                decrypted_title = decrypt_text(article['encrypted_title'], key)
                                article_md += f"**Decrypted Title:** {decrypted_title}\n\n"
                            except Exception as e:
                                article_md += f"**Error decrypting title:** {str(e)}\n\n"
                        
                        # Add encrypted title if requested
                        if include_encrypted and 'encrypted_title' in article:
                            article_md += f"**Encrypted Title:** {article['encrypted_title']}\n\n"
                        
                        markdown_content += article_md
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Exported {article_count} articles to {output_file}")
        return True
    
    except Exception as e:
        print(f"Error exporting to markdown: {str(e)}")
        return False
    
    finally:
        # Close MongoDB connection
        if mongo and "client" in mongo:
            mongo["client"].close()

def main():
    """Main function to run the script"""
    parser = argparse.ArgumentParser(description="Export MongoDB articles to a Markdown file")
    parser.add_argument("--output", type=str, default=None,
                        help="Output markdown file name (default: cybersecurity_articles_TIMESTAMP.md)")
    parser.add_argument("--collection", choices=["hackernews", "cybernews", "all"],
                        default="all", help="Collection to export (default: all)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Maximum number of articles to export per collection (default: all)")
    parser.add_argument("--include-encrypted", action="store_true",
                        help="Include encrypted titles in the output")
    parser.add_argument("--decrypt", action="store_true",
                        help="Include decrypted titles in the output")
    
    args = parser.parse_args()
    
    # Determine collections
    collections = None
    if args.collection == "all":
        collections = ["hackernews", "cybernews"]
    else:
        collections = args.collection
    
    # Export to markdown
    export_to_markdown(
        collections=collections,
        output_file=args.output,
        limit=args.limit,
        include_encrypted=args.include_encrypted,
        decrypt=args.decrypt
    )

if __name__ == "__main__":
    main() 