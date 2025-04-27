from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import re
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
def connect_to_mongodb(uri="mongodb+srv://ayushchy012:Chahuta3011@article-db.milce.mongodb.net/"):
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

# MongoDB client
mongo_client = connect_to_mongodb()
db = mongo_client["cybersaathi"]

@app.route('/')
def index():
    """Homepage - shows a list of all available articles with headlines"""
    # Get all tips collections
    collections = db.list_collection_names()
    tips_collections = [col for col in collections if col.startswith('tips_')]
    
    # Get all articles from all collections
    articles = []
    for collection_name in tips_collections:
        collection = db[collection_name]
        for doc in collection.find():
            # Extract tags if available
            tags = []
            if doc.get('tags') and doc.get('tags') != 'None':
                # Convert tags string to list
                tags_str = doc.get('tags', '')
                # Split by commas if there are any
                if ',' in tags_str:
                    tags = [tag.strip() for tag in tags_str.split(',')]
                else:
                    tags = [tags_str.strip()]
            
            articles.append({
                'article_id': doc.get('article_id', ''),
                'title': doc.get('title', 'Unknown'),
                'source': doc.get('source', 'Unknown'),
                'date': doc.get('date', 'Unknown'),
                'tags': tags
            })
    
    # Sort articles by date (most recent first) if possible
    try:
        articles.sort(key=lambda x: datetime.strptime(x['date'], '%d %B %Y'), reverse=True)
    except:
        # If date parsing fails, don't sort
        pass
    
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article_detail(article_id):
    """Detail view for a specific article"""
    # Get the article from the database
    article = get_article_by_id(article_id)
    
    if article:
        return render_template('article.html', article=article)
    else:
        return render_template('error.html', message=f"Article with ID {article_id} not found")

def get_article_by_id(article_id):
    """Get an article by its ID from any collection"""
    collections = db.list_collection_names()
    tips_collections = [col for col in collections if col.startswith('tips_')]
    
    for collection_name in tips_collections:
        collection = db[collection_name]
        article = collection.find_one({"article_id": article_id})
        if article:
            # Convert tags to list if they exist
            tags = []
            if article.get('tags') and article.get('tags') != 'None':
                tags_str = article.get('tags', '')
                if ',' in tags_str:
                    tags = [tag.strip() for tag in tags_str.split(',')]
                else:
                    tags = [tags_str.strip()]
            
            article['tags'] = tags
            return article
    
    return None

@app.route('/api/articles')
def api_articles():
    """API endpoint to get all articles"""
    collections = db.list_collection_names()
    tips_collections = [col for col in collections if col.startswith('tips_')]
    
    articles = []
    for collection_name in tips_collections:
        collection = db[collection_name]
        for doc in collection.find():
            # Convert MongoDB ObjectId to string
            doc['_id'] = str(doc['_id'])
            articles.append(doc)
    
    return jsonify(articles)

@app.route('/search')
def search():
    """Search for articles by title or tags"""
    query = request.args.get('q', '')
    if not query:
        return render_template('search.html', articles=[], query='')
    
    # Search in all tips collections
    collections = db.list_collection_names()
    tips_collections = [col for col in collections if col.startswith('tips_')]
    
    articles = []
    for collection_name in tips_collections:
        collection = db[collection_name]
        # Search in title or tags
        results = collection.find({
            '$or': [
                {'title': {'$regex': query, '$options': 'i'}},
                {'tags': {'$regex': query, '$options': 'i'}}
            ]
        })
        
        for doc in results:
            # Extract tags if available
            tags = []
            if doc.get('tags') and doc.get('tags') != 'None':
                tags_str = doc.get('tags', '')
                if ',' in tags_str:
                    tags = [tag.strip() for tag in tags_str.split(',')]
                else:
                    tags = [tags_str.strip()]
            
            articles.append({
                'article_id': doc.get('article_id', ''),
                'title': doc.get('title', 'Unknown'),
                'source': doc.get('source', 'Unknown'),
                'date': doc.get('date', 'Unknown'),
                'tags': tags
            })
    
    return render_template('search.html', articles=articles, query=query)

if __name__ == '__main__':
    app.run(debug=True) 