#!/usr/bin/env python3
"""
CyberSaathi Unified Workflow

This script provides a complete end-to-end workflow for CyberSaathi:
1. Scraping cybersecurity articles from multiple sites
2. Exporting data to markdown format
3. Summarizing articles using Ollama's llama3:8b model
4. Generating CISO tips (Do's and Don'ts) using Ollama
5. Storing all data in MongoDB for future retrieval

Run this script without arguments to execute the complete pipeline:
    python main.py

Options:
    --limit N          : Limit the number of articles to scrape (default: 10)
    --skip-scrape      : Skip the scraping step and use existing markdown
    --input-file FILE  : Use this markdown file instead of scraping
    --summary-file FILE: Use this summary file instead of generating new summaries
    --skip-summaries   : Skip the summarization step
    --skip-tips        : Skip the CISO tips generation step
    --skip-storage     : Skip storing data in MongoDB
    --verbose          : Show detailed output
"""

import os
import sys
import argparse
import importlib.util
import time
from datetime import datetime

# Import MongoDB functionality directly to avoid subprocess calls
try:
    from pymongo import MongoClient
    import requests
    from tqdm import tqdm
except ImportError:
    print("Error: Required modules not found. Please install dependencies:")
    print("pip install pymongo requests tqdm")
    sys.exit(1)

# Import functions from other scripts
try:
    # Import from Scraper.py
    sys.path.append(os.getcwd())
    from Scraper import scrape_hackernews, scrape_cybernews, MAX_ARTICLES, setup_mongodb
    
    # Use export_to_markdown functionality
    from export_to_markdown import export_to_markdown, format_article_to_markdown
    
    # Note: We'll import article_summarizer and ciso_tips_agent functions
    # directly within their respective processing functions to avoid 
    # any initialization issues
except ImportError as e:
    print(f"Error importing required modules: {str(e)}")
    print("Make sure all required script files are in the current directory")
    sys.exit(1)

def check_dependencies():
    """Check if all required modules are installed"""
    required_modules = [
        'pymongo', 'requests', 'tqdm', 'datetime', 'json', 're'
    ]
    
    missing = []
    for module in required_modules:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print("Missing required Python modules:")
        for module in missing:
            print(f"  - {module}")
        print("\nPlease install the required dependencies:")
        print("pip install " + " ".join(missing))
        return False
    
    return True

def check_ollama():
    """Check if Ollama is installed and running"""
    try:
        response = requests.get("http://localhost:11434/api/version", timeout=2)
        if response.status_code == 200:
            return True
        return False
    except:
        return False

def scrape_articles(limit=10, verbose=False):
    """Scrape articles from cybersecurity news sites"""
    print("\n[1/5] Scraping cybersecurity articles...")
    
    # Set global article limit
    global MAX_ARTICLES
    MAX_ARTICLES = limit
    
    try:
        # Run scrapers
        print(f"=== SCRAPING THE HACKER NEWS (max {limit} articles) ===")
        scrape_hackernews()
        
        print(f"\n=== SCRAPING CYBER NEWS (max {limit} articles) ===")
        scrape_cybernews()
        
        print("\n✅ Scraping completed successfully")
        return True
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        return False

def export_to_md(output_file=None, limit=None, verbose=False):
    """Export MongoDB data to markdown format"""
    print("\n[2/5] Exporting articles to markdown...")
    
    # Generate timestamp for output file if not provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"cybersecurity_articles_{timestamp}.md"
    
    # Export articles from MongoDB to markdown
    success = export_to_markdown(
        collections=["hackernews", "cybernews"],
        output_file=output_file,
        limit=limit
    )
    
    if success:
        print(f"✅ Articles exported to markdown: {output_file}")
        return output_file
    else:
        print("❌ Failed to export articles to markdown")
        return None

def summarize_articles(input_file, output_file=None, verbose=False):
    """Summarize articles using Ollama's llama3:8b model"""
    print("\n[3/5] Summarizing articles...")
    
    # Generate output file name if not provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"article_summaries_{timestamp}.md"
    
    # Import functions from article_summarizer.py
    try:
        from article_summarizer import read_markdown_file, summarize_with_ollama, create_summary_markdown, check_ollama_availability
    except ImportError:
        print("Error importing functions from article_summarizer.py")
        return None
    
    try:
        # Check if Ollama is available
        if not check_ollama_availability():
            print("Cannot proceed with summarization without Ollama service.")
            return None
        
        # Read and parse the markdown file
        header, articles = read_markdown_file(input_file)
        
        # Summarize articles (single-threaded to avoid Ollama overload)
        print(f"Starting summarization of {len(articles)} articles...")
        results = []
        
        for i, article in enumerate(articles):
            print(f"Summarizing article {i+1}/{len(articles)}: {article['title']}")
            result = summarize_with_ollama(article)
            results.append(result)
        
        # Create summary markdown file
        output_path = create_summary_markdown(header, results, output_file)
        print(f"✅ Summarization completed. Output saved to: {output_path}")
        
        # Store summaries in MongoDB (optional step, not in original workflow)
        # This step could be added here if needed
        
        return output_path
    
    except Exception as e:
        print(f"Error during summarization: {str(e)}")
        return None

def generate_ciso_tips(input_file, output_file=None, verbose=False):
    """Generate CISO tips from article summaries"""
    print("\n[4/5] Generating CISO tips...")
    
    # Generate output file name if not provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"ciso_tips_{timestamp}.md"
    
    # Import functions from ciso_tips_agent.py
    try:
        from ciso_tips_agent import extract_articles_from_markdown, generate_tips_with_ollama, format_tips_as_markdown
    except ImportError:
        print("Error importing functions from ciso_tips_agent.py")
        return None
    
    try:
        # Extract articles from the markdown file
        articles = extract_articles_from_markdown(input_file)
        
        # Generate tips for each article
        print(f"Generating tips for {len(articles)} articles...")
        tips_collection = []
        
        for i, article in enumerate(articles):
            print(f"Processing article {i+1}/{len(articles)}: {article['title']}")
            tips = generate_tips_with_ollama(article)
            tips_collection.append(tips)
        
        # Format and save tips as markdown
        format_tips_as_markdown(tips_collection, output_file)
        
        print(f"✅ CISO tips generation completed. Output saved to: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"Error generating CISO tips: {str(e)}")
        return None

def store_tips_in_mongodb(input_file, verbose=False):
    """Store CISO tips in MongoDB"""
    print("\n[5/5] Storing tips in MongoDB...")
    
    # Import functions from store_tips.py
    try:
        from store_tips import connect_to_mongodb, parse_tips_markdown, store_tips_in_mongodb
    except ImportError:
        print("Error importing functions from store_tips.py")
        return False
    
    try:
        # Connect to MongoDB
        client = connect_to_mongodb()
        
        # Parse the tips markdown file
        articles = parse_tips_markdown(input_file)
        
        # Store articles in MongoDB
        store_tips_in_mongodb(client, articles)
        
        print("✅ Tips successfully stored in MongoDB")
        return True
    
    except Exception as e:
        print(f"Error storing tips in MongoDB: {str(e)}")
        return False
    
    finally:
        # Close MongoDB connection if it exists
        if 'client' in locals():
            client.close()

def main():
    """Main function to run the complete workflow"""
    parser = argparse.ArgumentParser(description="CyberSaathi Unified Workflow")
    parser.add_argument("--limit", type=int, default=10, 
                        help="Maximum number of articles to scrape from each site (default: 10)")
    parser.add_argument("--skip-scrape", action="store_true",
                        help="Skip the scraping step and use existing markdown")
    parser.add_argument("--input-file", type=str,
                        help="Use this markdown file instead of scraping")
    parser.add_argument("--summary-file", type=str,
                        help="Use this summary file instead of generating new summaries")
    parser.add_argument("--skip-summaries", action="store_true",
                        help="Skip the article summarization step")
    parser.add_argument("--skip-tips", action="store_true",
                        help="Skip the CISO tips generation step")
    parser.add_argument("--skip-storage", action="store_true",
                        help="Skip storing data in MongoDB")
    parser.add_argument("--verbose", action="store_true",
                        help="Show detailed output")
    
    args = parser.parse_args()
    
    # Print banner
    print("\n========================================================")
    print("    CyberSaathi - Complete Cybersecurity Workflow")
    print("========================================================\n")
    
    # Check dependencies
    print("Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    if not check_ollama():
        print("Warning: Ollama is not running or not accessible.")
        print("Please start Ollama to enable article summarization and CISO tips generation.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    start_time = time.time()
    
    # Step 1-2: Scrape articles and export to markdown
    input_file = args.input_file
    if not args.skip_scrape and not input_file:
        # Scrape articles
        if scrape_articles(limit=args.limit, verbose=args.verbose):
            # Export to markdown
            input_file = export_to_md(limit=args.limit, verbose=args.verbose)
            if not input_file:
                print("Failed to export articles to markdown. Exiting.")
                sys.exit(1)
    elif args.skip_scrape and not input_file:
        print("Error: --skip-scrape option requires --input-file. Please specify an input file.")
        sys.exit(1)
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    print(f"Using input file: {input_file}")
    
    # Step 3: Summarize articles
    summary_file = args.summary_file
    if args.skip_summaries:
        print("Skipping article summarization...")
        if not summary_file:
            # If summary file not provided, use input file as source for tips
            summary_file = input_file
    else:
        if not summary_file:
            # Generate summaries
            summary_file = summarize_articles(input_file, verbose=args.verbose)
            if not summary_file:
                print("Failed to summarize articles. Exiting.")
                sys.exit(1)
        else:
            # Check if provided summary file exists
            if not os.path.exists(summary_file):
                print(f"Error: Summary file '{summary_file}' not found")
                sys.exit(1)
    
    print(f"Using summary file: {summary_file}")
    
    # Step 4: Generate CISO tips
    tips_file = None
    if not args.skip_tips:
        tips_file = generate_ciso_tips(summary_file, verbose=args.verbose)
        if not tips_file:
            print("Failed to generate CISO tips. Exiting.")
            sys.exit(1)
    else:
        print("Skipping CISO tips generation...")
    
    # Step 5: Store tips in MongoDB
    if not args.skip_storage and tips_file:
        if not store_tips_in_mongodb(tips_file, verbose=args.verbose):
            print("Failed to store tips in MongoDB.")
    elif args.skip_storage:
        print("Skipping storage in MongoDB...")
    
    # Print completion message
    elapsed_time = time.time() - start_time
    print("\n========================================================")
    print("    CyberSaathi Workflow Completed Successfully!")
    print("========================================================")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    
    if input_file:
        print(f"Articles file: {input_file}")
    if summary_file:
        print(f"Article summaries: {summary_file}")
    if tips_file:
        print(f"CISO tips: {tips_file}")
    
    print("\nYou can now query the tips using:")
    print("python query_tips.py --list")
    print("python query_tips.py --id <article_id>")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1) 