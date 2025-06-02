# database.py
from pymongo import MongoClient
from config import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME

# Initialize MongoDB client
client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def find_movie(query):
    """Search for a movie in the database by title."""
    try:
        return collection.find_one({"title": {"$regex": query, "$options": "i"}})
    except Exception as e:
        print(f"Error finding movie: {e}")
        return None

def insert_movie(movie_data):
    """Insert a movie into the database (for setup purposes)."""
    try:
        collection.insert_one(movie_data)
        print(f"Inserted movie: {movie_data['title']}")
    except Exception as e:
        print(f"Error inserting movie: {e}")

def close_connection():
    """Close the MongoDB connection."""
    client.close()
    print("MongoDB connection closed.")