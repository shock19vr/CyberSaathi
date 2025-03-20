#!/usr/bin/env python3
"""
Script to store article summaries in MongoDB with date-wise collections.
Each article summary is stored with its original article ID for reference.
"""

import os
import re
import argparse
from datetime import datetime
from pymongo import MongoClient
from typing import Dict, List, Any

def connect_to_mongodb(uri: str = "mongodb+srv://ayushchy012:Chahuta3011@article-db.milce.mongodb.net/") -> MongoClient:
    """Establish connection to MongoDB"""
    try:
        client = MongoClient(uri)
        # Test the connection
        client.server_info()
        print("Successfully connected to MongoDB")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        raise

def parse_summary_markdown(file_path: str) -> List[Dict[str, Any]]:
    """Parse the summary markdown file and extract article data"""
    print(f"Reading summary markdown file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into individual articles
    article_sections = re.split(r'\n## \d+\.', content)
    
    # First section contains header information
    header = article_sections[0]
    article_sections = article_sections[1:]
    
    # Extract generation date from header
    date_match = re.search(r'Generated on: (\d{4}-\d{2}-\d{2})', header)
    if not date_match:
        raise ValueError("Could not find generation date in markdown file")
    generation_date = date_match.group(1)
    
    # Process each article
    articles = []
    for i, section in enumerate(article_sections):
        # Clean up the section
        section = section.strip()
        if not section:
            continue
        
        # Extract title (first line is the title)
        title = section.split('\n')[0].strip()
        
        # Extract metadata
        metadata = {}
        metadata_matches = re.findall(r'\*\*(.*?):\*\* (.*?)$', section, re.MULTILINE)
        for key, value in metadata_matches:
            metadata[key.lower()] = value.strip()
        
        # Extract summary
        summary_match = re.search(r'### Summary\n\n(.*?)(?:\n\n---|\Z)', section, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""
        
        # Create article document
        article = {
            'index': i + 1,
            'title': title,
            'summary': summary,
            'generation_date': generation_date,
            'metadata': metadata
        }
        
        articles.append(article)
    
    print(f"Extracted {len(articles)} article summaries")
    return articles

def store_summaries_in_mongodb(client: MongoClient, articles: List[Dict[str, Any]], db_name: str = "cybersaathi"):
    """Store article summaries in MongoDB with date-wise collections"""
    db = client[db_name]
    
    # Group articles by article date (from metadata) instead of generation date
    articles_by_date = {}
    for article in articles:
        # Try to get the article date from metadata
        article_date = None
        if 'date' in article['metadata']:
            # Parse the date from the metadata - format may be like "20 March 2025"
            try:
                date_str = article['metadata']['date']
                # Try to parse various date formats
                date_formats = [
                    "%d %B %Y",  # 20 March 2025
                    "%B %d, %Y", # March 20, 2025
                    "%Y-%m-%d",  # 2025-03-20
                    "%d/%m/%Y",  # 20/03/2025
                    "%m/%d/%Y"   # 03/20/2025
                ]
                
                for fmt in date_formats:
                    try:
                        parsed_date = datetime.strptime(date_str, fmt)
                        article_date = parsed_date.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        continue
            except Exception as e:
                print(f"Warning: Could not parse date '{date_str}' for article '{article['title']}': {str(e)}")
        
        # If we couldn't parse the article date, use generation date as fallback
        if not article_date:
            article_date = article['generation_date']
            print(f"Using generation date for article '{article['title']}' as fallback")
        
        # Add to appropriate date group
        if article_date not in articles_by_date:
            articles_by_date[article_date] = []
        articles_by_date[article_date].append(article)
    
    # Store articles in date-wise collections
    for date, date_articles in articles_by_date.items():
        collection_name = f"summaries_{date.replace('-', '_')}"
        collection = db[collection_name]
        
        # Prepare documents for insertion
        documents = []
        for article in date_articles:
            # Create a document with the article data
            doc = {
                'article_id': article['metadata'].get('id', f"article_{article['index']}"),
                'title': article['title'],
                'summary': article['summary'],
                'source': article['metadata'].get('source', 'Unknown'),
                'url': article['metadata'].get('url', 'Unknown'),
                'tags': article['metadata'].get('tags', 'None'),
                'date': article['metadata'].get('date', 'Unknown'),
                'index': article['index'],
                'created_at': datetime.now()
            }
            documents.append(doc)
        
        # Insert documents into the collection
        if documents:
            result = collection.insert_many(documents)
            print(f"Stored {len(result.inserted_ids)} articles in collection '{collection_name}'")
        else:
            print(f"No articles to store in collection '{collection_name}'")

def main():
    """Main function to run the storage process"""
    parser = argparse.ArgumentParser(description="Store article summaries in MongoDB with date-wise collections")
    parser.add_argument("--input", type=str, required=True,
                        help="Input markdown file containing article summaries")
    parser.add_argument("--mongodb-uri", type=str, 
                        default="mongodb+srv://ayushchy012:Chahuta3011@article-db.milce.mongodb.net/",
                        help="MongoDB connection URI (default: MongoDB Atlas connection)")
    parser.add_argument("--db-name", type=str, default="cybersaathi",
                        help="MongoDB database name (default: cybersaathi)")
    
    args = parser.parse_args()
    
    try:
        # Connect to MongoDB
        client = connect_to_mongodb(args.mongodb_uri)
        
        # Parse the summary markdown file
        articles = parse_summary_markdown(args.input)
        
        # Store articles in MongoDB
        store_summaries_in_mongodb(client, articles, args.db_name)
        
        print("\nSuccessfully completed storing article summaries in MongoDB!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        raise
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    main() 