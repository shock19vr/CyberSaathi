"""
CyberSaathi Main Processor

This script combines all CyberSaathi functionality into a single pipeline:
1. Web scraping (collects articles from cybersecurity news sites)
2. Export to markdown (converts articles to markdown format)
3. Article summarization
4. CISO tips generation
5. MongoDB storage

Usage:
    # Run complete pipeline including scraper:
    python cybersaathi_main.py
    
    # Use an existing markdown file instead of scraping:
    python cybersaathi_main.py <articles_file.md> [options]
    python cybersaathi_main.py --input <articles_file.md> [options]

Options:
    --skip-scraper        Skip the web scraping step (requires input file)
    --skip-summaries      Skip the article summarization step
    --summary-file FILE   Use this summary file instead of generating a new one
    --skip-checks         Skip dependency checks
"""

import argparse
import os
import sys
import time
import subprocess
from datetime import datetime
import importlib.util

def check_dependencies():
    """Check if all required modules are installed"""
    required_modules = [
        'pymongo', 'requests', 'colorama', 'markdown', 
        'tqdm', 'dateutil', 'ollama', 'selenium'
    ]
    
    missing = []
    for module in required_modules:
        if importlib.util.find_spec(module) is None:
            missing.append(module)
    
    if missing:
        print("Missing required Python modules:")
        for module in missing:
            print(f"  - {module}")
        print("\nPlease install the required dependencies:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def check_ollama():
    """Check if Ollama is installed and running"""
    import requests
    try:
        response = requests.get("http://localhost:11434/api/version", timeout=2)
        if response.status_code == 200:
            return True
        return False
    except:
        return False

def check_mongodb():
    """Check if MongoDB is accessible"""
    from pymongo import MongoClient
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        client.server_info()
        return True
    except:
        return False

def run_article_summarizer(input_file):
    """Run the article summarizer script"""
    from importlib import import_module
    
    # Generate timestamp for output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"article_summaries_{timestamp}.md"
    
    print("\n[1/3] Running Article Summarizer...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    
    # Check if article_summarizer.py exists
    if not os.path.exists("article_summarizer.py"):
        print("Error: article_summarizer.py not found in the current directory")
        sys.exit(1)
    
    # Run the summarizer as a subprocess to ensure clean execution
    result = subprocess.run(
        ["python", "article_summarizer.py", "--input", input_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error running article_summarizer.py: {result.stderr}")
        sys.exit(1)
    
    # Extract the output file from the output
    for line in result.stdout.split('\n'):
        if "Summary markdown file created:" in line:
            output_file = line.split(":")[-1].strip()
            break
    
    print(f"✅ Article summarization completed")
    return output_file

def run_ciso_tips_generator(input_file):
    """Run the CISO tips generator script"""
    # Generate timestamp for output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"ciso_tips_{timestamp}.md"
    
    print("\n[2/3] Generating CISO Tips...")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    
    # Check if ciso_tips_agent.py exists
    if not os.path.exists("ciso_tips_agent.py"):
        print("Error: ciso_tips_agent.py not found in the current directory")
        sys.exit(1)
    
    # Run the tips generator as a subprocess
    result = subprocess.run(
        ["python", "ciso_tips_agent.py", "--input", input_file, "--output", output_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error running ciso_tips_agent.py: {result.stderr}")
        sys.exit(1)
    
    print(f"✅ CISO tips generation completed")
    return output_file

def run_tips_storage(input_file):
    """Run the tips storage script"""
    print("\n[3/3] Storing CISO Tips in MongoDB...")
    print(f"Input: {input_file}")
    
    # Check if store_tips.py exists
    if not os.path.exists("store_tips.py"):
        print("Error: store_tips.py not found in the current directory")
        sys.exit(1)
    
    # Run the storage script as a subprocess
    result = subprocess.run(
        ["python", "store_tips.py", "--input", input_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error running store_tips.py: {result.stderr}")
        sys.exit(1)
    
    print(f"✅ Tips storage completed")
    return True

def run_scraper():
    """Run the web scraper to collect articles"""
    # Generate timestamp for output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"cybersecurity_articles_{timestamp}.md"
    
    print("\n[1/5] Running Web Scraper...")
    
    # Check if Scraper.py exists
    if not os.path.exists("Scraper.py"):
        print("Error: Scraper.py not found in the current directory")
        sys.exit(1)
    
    # Run the scraper as a subprocess
    result = subprocess.run(
        ["python", "Scraper.py", "--limit", "10"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error running Scraper.py: {result.stderr}")
        sys.exit(1)
    
    print(f"✅ Web scraping completed")
    
    # Run export_to_markdown.py to generate markdown file
    print("\n[2/5] Exporting articles to markdown...")
    
    # Check if export_to_markdown.py exists
    if not os.path.exists("export_to_markdown.py"):
        print("Error: export_to_markdown.py not found in the current directory")
        sys.exit(1)
    
    # Run the export script as a subprocess
    result = subprocess.run(
        ["python", "export_to_markdown.py", "--output", output_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error running export_to_markdown.py: {result.stderr}")
        sys.exit(1)
    
    print(f"✅ Articles exported to markdown: {output_file}")
    return output_file

def main():
    """Main function to run the entire CyberSaathi pipeline"""
    # Print arguments for debugging
    print("Arguments received:", sys.argv)
    
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="CyberSaathi - Complete Cybersecurity Assistant Pipeline")
    
    # Add positional argument for input file (optional)
    parser.add_argument("input_file", type=str, nargs="?",
                       help="Optional: Input markdown file containing cybersecurity articles (if not provided, scraper will run)")
    
    # Keep the --input parameter for backward compatibility
    parser.add_argument("--input", type=str, 
                        help="Optional: Input markdown file containing cybersecurity articles (if not provided, scraper will run)")
    
    parser.add_argument("--skip-scraper", action="store_true",
                        help="Skip the web scraping step (requires input file)")
    parser.add_argument("--skip-summaries", action="store_true",
                        help="Skip the article summarization step")
    parser.add_argument("--summary-file", type=str,
                        help="Use this summary file instead of generating a new one")
    parser.add_argument("--skip-checks", action="store_true",
                        help="Skip dependency checks")
    
    args = parser.parse_args()
    
    # Print parsed arguments for debugging
    print("Parsed arguments:", vars(args))
    
    # Get input file from arguments
    input_file = args.input_file if args.input_file else args.input
    
    # Print banner
    print("\n========================================================")
    print("    CyberSaathi - Cybersecurity Assistant Pipeline")
    print("========================================================\n")
    
    # Check dependencies
    if not args.skip_checks:
        print("Checking dependencies...")
        if not check_dependencies():
            sys.exit(1)
        
        if not check_ollama():
            print("Warning: Ollama is not running or not accessible.")
            print("Please start Ollama to enable CISO tips generation.")
            response = input("Continue anyway? (y/n): ")
            if response.lower() != 'y':
                sys.exit(1)
        
        if not check_mongodb():
            print("Warning: MongoDB is not running or not accessible.")
            print("Please start MongoDB to enable tips storage.")
            response = input("Continue anyway? (y/n): ")
            if response.lower() != 'y':
                sys.exit(1)
    
    try:
        start_time = time.time()
        
        # Step 1-2: Web scraping and markdown export (optional)
        if not input_file and not args.skip_scraper:
            # No input file provided, run the scraper to generate it
            input_file = run_scraper()
        elif args.skip_scraper and not input_file:
            # Skip scraper requested but no input file provided
            parser.print_help()
            print("\nError: --skip-scraper option requires an input file. Please specify an input file.")
            sys.exit(1)
        elif not input_file:
            # No input file and skip scraper not explicitly requested, run scraper
            input_file = run_scraper()
        
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found")
            sys.exit(1)
            
        print(f"Using input file: {input_file}")
        
        # Step 3: Article Summarization (optional)
        if args.skip_summaries:
            print("[3/5] Skipping article summarization...")
            summary_file = input_file
        elif args.summary_file:
            print(f"[3/5] Using provided summary file: {args.summary_file}")
            if not os.path.exists(args.summary_file):
                print(f"Error: Summary file '{args.summary_file}' not found")
                sys.exit(1)
            summary_file = args.summary_file
        else:
            summary_file = run_article_summarizer(input_file)
        
        # Step 4: CISO Tips Generation
        tips_file = run_ciso_tips_generator(summary_file)
        
        # Step 5: Store Tips in MongoDB
        run_tips_storage(tips_file)
        
        # Print completion message
        elapsed_time = time.time() - start_time
        print("\n========================================================")
        print("    CyberSaathi Pipeline Completed Successfully!")
        print("========================================================")
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        
        if not args.skip_scraper and not args.input_file and not args.input:
            print(f"Generated articles: {input_file}")
            
        print(f"Article summaries: {summary_file}")
        print(f"CISO tips: {tips_file}")
        print("\nYou can now query the tips using:")
        print("python query_tips.py --list")
        print("python query_tips.py --id <article_id>")
        
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 