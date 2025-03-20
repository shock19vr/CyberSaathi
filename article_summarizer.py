#!/usr/bin/env python3
"""
Article Summarization Agent using Ollama's llama3:8b

This script takes a markdown file containing articles, processes each article
using the llama3:8b model via Ollama, and generates concise summaries.
The output is a new markdown file with the summarized content.
"""

import os
import re
import json
import time
import argparse
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def read_markdown_file(file_path):
    """Read and parse the markdown file into articles"""
    print(f"Reading markdown file: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into individual articles
    article_sections = re.split(r'\n## \d+\.', content)
    
    # First section contains header information, not an article
    header = article_sections[0]
    article_sections = article_sections[1:]
    
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
        
        # Extract content
        content_section = re.search(r'### Content:\s*\n\n(.*?)(?:\n\n---|\Z)', section, re.DOTALL)
        content = content_section.group(1).strip() if content_section else ""
        
        # Create article object
        article = {
            'index': i + 1,
            'title': title,
            'content': content
        }
        article.update(metadata)
        
        articles.append(article)
    
    print(f"Extracted {len(articles)} articles from markdown file")
    return header, articles

def summarize_with_ollama(article, max_retries=3, retry_delay=2):
    """Summarize an article using Ollama's llama3:8b model"""
    # Prepare the prompt
    prompt = f"""
You are a professional article summarizer. Summarize the following article in 3-4 concise paragraphs.
Focus on the key points, main insights, and important details.
Keep your summary informative but concise.

Title: {article['title']}
Date: {article.get('date', 'Unknown')}
Source: {article.get('source', 'Unknown')}
Tags: {article.get('tags', 'None')}

Content:
{article['content']}

Your summary:
"""

    # Set up the API request
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3:8b",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.1,  # Low temperature for more factual responses
        "max_tokens": 1024
    }
    
    # Try to get summary with retries
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            result = response.json()
            
            if "response" in result:
                # Clean up the response, removing any markdown formatting the model might add
                summary = result["response"].strip()
                summary = re.sub(r'^#+\s*Summary:?\s*$', '', summary, flags=re.MULTILINE)
                summary = re.sub(r'^\s*\*\*Summary:?\*\*\s*$', '', summary, flags=re.MULTILINE)
                summary = summary.strip()
                
                return {
                    "status": "success",
                    "summary": summary,
                    "article": article
                }
            else:
                print(f"Error: Unexpected response format from Ollama for article '{article['title']}'")
        
        except requests.exceptions.RequestException as e:
            print(f"Request error on attempt {attempt+1} for article '{article['title']}': {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return {
                    "status": "error",
                    "error": str(e),
                    "article": article
                }
        
        except Exception as e:
            print(f"Unexpected error on attempt {attempt+1} for article '{article['title']}': {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return {
                    "status": "error",
                    "error": str(e),
                    "article": article
                }
    
    return {
        "status": "error",
        "error": "Max retries exceeded",
        "article": article
    }

def create_summary_markdown(header, summaries, output_file=None):
    """Create a markdown file with article summaries"""
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"article_summaries_{timestamp}.md"
    
    # Prepare the output content
    content = f"{header}\n\n# Article Summaries\n\n"
    content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    content += f"Number of summarized articles: {len(summaries)}\n\n"
    
    # Sort summaries by index
    summaries.sort(key=lambda x: x["article"]["index"])
    
    # Add each summary
    for result in summaries:
        article = result["article"]
        
        # Article header
        content += f"## {article['index']}. {article['title']}\n\n"
        
        # Metadata
        content += f"**Source:** {article.get('source', 'Unknown')}\n"
        content += f"**Date:** {article.get('date', 'Unknown')}\n"
        content += f"**URL:** {article.get('url', 'Unknown')}\n"
        if "id" in article:
            content += f"**ID:** {article['id']}\n"
        content += f"**Tags:** {article.get('tags', 'None')}\n\n"
        
        # Summary
        content += "### Summary\n\n"
        if result["status"] == "success":
            content += f"{result['summary']}\n\n"
        else:
            content += f"*Error generating summary: {result.get('error', 'Unknown error')}*\n\n"
        
        # Separator
        content += "---\n\n"
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created summary markdown file: {output_file}")
    return output_file

def check_ollama_availability():
    """Check if Ollama is running and the llama3:8b model is available"""
    try:
        # Check if Ollama service is running
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        response.raise_for_status()
        
        # Check if llama3:8b model is available
        models = response.json().get("models", [])
        for model in models:
            if model["name"] == "llama3:8b":
                return True
        
        print("Warning: llama3:8b model not found in Ollama. Will attempt to pull it...")
        
        # Try to pull the model
        pull_response = requests.post(
            "http://localhost:11434/api/pull", 
            json={"name": "llama3:8b"}, 
            timeout=600
        )
        pull_response.raise_for_status()
        return True
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama service. Make sure Ollama is running on localhost:11434")
        return False
    except Exception as e:
        print(f"Error checking Ollama availability: {str(e)}")
        return False

def main():
    """Main function to run the summarization agent"""
    parser = argparse.ArgumentParser(description="Summarize articles from a markdown file using Ollama's llama3:8b model")
    parser.add_argument("--input", type=str, required=True,
                        help="Input markdown file containing articles")
    parser.add_argument("--output", type=str, default=None,
                        help="Output markdown file for summaries (default: article_summaries_TIMESTAMP.md)")
    parser.add_argument("--max-workers", type=int, default=1,
                        help="Maximum number of concurrent summarization tasks (default: 1)")
    
    args = parser.parse_args()
    
    # Check if Ollama is available
    if not check_ollama_availability():
        print("Cannot proceed without Ollama service.")
        return
    
    # Read and parse the markdown file
    header, articles = read_markdown_file(args.input)
    
    # Summarize articles with multi-threading
    print(f"Starting summarization of {len(articles)} articles with {args.max_workers} workers...")
    results = []
    
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_to_article = {executor.submit(summarize_with_ollama, article): article for article in articles}
        
        for future in as_completed(future_to_article):
            article = future_to_article[future]
            try:
                result = future.result()
                results.append(result)
                status = "✓" if result["status"] == "success" else "✗"
                print(f"[{status}] Processed article {article['index']}: {article['title'][:40]}...")
            except Exception as e:
                print(f"[✗] Error processing article {article['index']}: {str(e)}")
                results.append({
                    "status": "error",
                    "error": str(e),
                    "article": article
                })
    
    # Create the output markdown file
    output_file = create_summary_markdown(header, results, args.output)
    
    # Print statistics
    success_count = sum(1 for r in results if r["status"] == "success")
    error_count = len(results) - success_count
    print(f"\nSummary: Successfully summarized {success_count}/{len(results)} articles")
    if error_count > 0:
        print(f"Encountered errors with {error_count} articles")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    main() 