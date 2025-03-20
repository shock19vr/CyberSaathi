"""
CISO Tips Agent

This script extracts context from cybersecurity articles and uses llama3:8b 
to generate security do's and don'ts for non-technical users.
"""

import argparse
import re
import json
import requests
import os
from typing import Dict, List, Any
from datetime import datetime

def extract_articles_from_markdown(file_path: str) -> List[Dict[str, Any]]:
    """Extract full article content from markdown file"""
    print(f"Reading markdown file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match individual articles in markdown
    article_pattern = r'## (\d+)\. (.+?)(?=\n## \d+\.|\Z)'
    articles_raw = re.findall(article_pattern, content, re.DOTALL)
    
    articles = []
    for idx, article_content in articles_raw:
        # Extract title and content
        lines = article_content.strip().split('\n')
        title = lines[0].strip()
        
        # Extract metadata
        metadata = {}
        metadata_section = ""
        content_section = ""
        
        metadata_started = False
        content_started = False
        
        for line in lines[1:]:
            if line.startswith('**') and ':**' in line:
                metadata_started = True
                metadata_section += line + "\n"
            elif line.startswith('### Content') or line.startswith('### Summary'):
                metadata_started = False
                content_started = True
            elif metadata_started:
                metadata_section += line + "\n"
            elif content_started:
                content_section += line + "\n"
        
        # Parse metadata
        metadata_matches = re.findall(r'\*\*(.*?):\*\* (.*?)$', metadata_section, re.MULTILINE)
        for key, value in metadata_matches:
            metadata[key.lower()] = value.strip()
        
        # Create article object
        article = {
            'index': int(idx),
            'title': title,
            'content': content_section.strip(),
            'metadata': metadata
        }
        
        articles.append(article)
    
    print(f"Extracted {len(articles)} articles")
    return articles

def generate_tips_with_ollama(article: Dict[str, Any], model: str = "llama3:8b") -> Dict[str, Any]:
    """Generate CISO tips using Ollama's llama3:8b model"""
    # Construct prompt for the Ollama model
    prompt = f"""
You are acting as a Chief Information Security Officer (CISO) providing cybersecurity advice to non-technical users.
Based on the following article, create a list of practical "DO's" and "DON'Ts" for ordinary people to follow.
Use simple, non-technical language that anyone can understand.

Article Title: {article['title']}
Article Content:
{article['content']}

Your response should be structured as follows:
1. A very brief summary of the key security issue (2-3 sentences maximum)
2. A list of 3-5 "DO's" - specific actions people should take
3. A list of 3-5 "DON'Ts" - specific actions people should avoid

Your response should be in the following JSON format:
{{
  "summary": "Brief summary here",
  "dos": ["Do this", "Do that", ...],
  "donts": ["Don't do this", "Don't do that", ...]
}}

Remember: Keep everything simple, practical, and actionable for non-technical users.
"""

    # Call Ollama API
    try:
        response = requests.post('http://localhost:11434/api/generate', 
                                json={
                                    'model': model,
                                    'prompt': prompt,
                                    'stream': False,
                                    'options': {
                                        'temperature': 0.2,  # Low temperature for more focused answers
                                        'top_p': 0.95,
                                        'top_k': 40
                                    }
                                })
        
        if response.status_code == 200:
            # Extract the response
            result = response.json()
            response_text = result.get('response', '')
            
            # Try to extract JSON from the response
            try:
                # Find JSON object in the response
                json_match = re.search(r'({.*})', response_text.replace('\n', ' '), re.DOTALL)
                if json_match:
                    tips_json = json.loads(json_match.group(1))
                else:
                    # If no JSON found, try to parse structured text
                    summary_match = re.search(r'summary["\s:]+([^"]+)', response_text, re.IGNORECASE)
                    dos_match = re.findall(r'do[^\n\d:"]*["\s:]+([^",\[\]]+)', response_text, re.IGNORECASE)
                    donts_match = re.findall(r'don[^\n\d:"]*["\s:]+([^",\[\]]+)', response_text, re.IGNORECASE)
                    
                    tips_json = {
                        "summary": summary_match.group(1).strip() if summary_match else "No summary available.",
                        "dos": [item.strip() for item in dos_match] if dos_match else ["No specific dos provided."],
                        "donts": [item.strip() for item in donts_match] if donts_match else ["No specific don'ts provided."]
                    }
                
                return {
                    "article_id": article['metadata'].get('id', f"article_{article['index']}"),
                    "title": article['title'],
                    "source": article['metadata'].get('source', 'Unknown'),
                    "date": article['metadata'].get('date', 'Unknown'),
                    "tags": article['metadata'].get('tags', 'None'),
                    "tips": tips_json,
                    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            except Exception as e:
                print(f"Error parsing Ollama response for article '{article['title']}': {str(e)}")
                print(f"Raw response: {response_text}")
                return {
                    "article_id": article['metadata'].get('id', f"article_{article['index']}"),
                    "title": article['title'],
                    "error": f"Failed to parse response: {str(e)}",
                    "raw_response": response_text
                }
        else:
            print(f"Error from Ollama API: {response.status_code} - {response.text}")
            return {
                "article_id": article['metadata'].get('id', f"article_{article['index']}"),
                "title": article['title'],
                "error": f"Ollama API error: {response.status_code}",
                "raw_response": response.text
            }
    except Exception as e:
        print(f"Exception calling Ollama API: {str(e)}")
        return {
            "article_id": article['metadata'].get('id', f"article_{article['index']}"),
            "title": article['title'],
            "error": f"API call exception: {str(e)}"
        }

def format_tips_as_markdown(tips_collection: List[Dict[str, Any]], output_file: str):
    """Format the tips as a markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("# CISO Security Tips for Non-Technical Users\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Number of articles: {len(tips_collection)}\n\n")
        
        # Write tips for each article
        for i, tips in enumerate(tips_collection):
            f.write(f"## {i+1}. {tips['title']}\n\n")
            
            # Write metadata
            f.write(f"**Source:** {tips.get('source', 'Unknown')}\n")
            f.write(f"**Date:** {tips.get('date', 'Unknown')}\n")
            if 'tags' in tips and tips['tags'] != 'None':
                f.write(f"**Tags:** {tips['tags']}\n")
            
            # Check if there was an error
            if 'error' in tips:
                f.write(f"\n### Error\n\n{tips['error']}\n\n")
                if 'raw_response' in tips:
                    f.write(f"Raw response: {tips['raw_response']}\n\n")
                continue
            
            # Write summary and tips
            if 'tips' in tips:
                # Summary
                if 'summary' in tips['tips']:
                    f.write(f"\n### Key Security Issue\n\n{tips['tips']['summary']}\n\n")
                
                # DO's
                if 'dos' in tips['tips'] and tips['tips']['dos']:
                    f.write("### DO's\n\n")
                    for do_item in tips['tips']['dos']:
                        f.write(f"✅ {do_item}\n\n")
                
                # DON'Ts
                if 'donts' in tips['tips'] and tips['tips']['donts']:
                    f.write("### DON'Ts\n\n")
                    for dont_item in tips['tips']['donts']:
                        f.write(f"❌ {dont_item}\n\n")
            
            # Add separator
            f.write("---\n\n")
    
    print(f"Tips saved to {output_file}")

def main():
    """Main function to run the CISO tips agent"""
    parser = argparse.ArgumentParser(description="CISO Tips Agent - Generate security do's and don'ts for non-technical users")
    parser.add_argument("--input", type=str, required=True,
                        help="Input markdown file containing full article content")
    parser.add_argument("--output", type=str, default=f"ciso_tips_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        help="Output markdown file for the generated tips")
    parser.add_argument("--model", type=str, default="llama3:8b",
                        help="Ollama model to use (default: llama3:8b)")
    
    args = parser.parse_args()
    
    try:
        # Extract articles from the markdown file
        articles = extract_articles_from_markdown(args.input)
        
        # Generate tips for each article
        print(f"Generating tips using Ollama model: {args.model}")
        tips_collection = []
        
        for i, article in enumerate(articles):
            print(f"Processing article {i+1}/{len(articles)}: {article['title']}")
            tips = generate_tips_with_ollama(article, args.model)
            tips_collection.append(tips)
        
        # Format and save tips as markdown
        format_tips_as_markdown(tips_collection, args.output)
        
        print(f"\nSuccessfully generated CISO tips for {len(articles)} articles!")
        print(f"Tips saved to: {args.output}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        raise

if __name__ == "__main__":
    main() 