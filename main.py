# main.py
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION
from handlers.start_handler import register_start_handler
from handlers.search_handler import register_search_handler
from handlers.callback_handler import register_callback_handler
from database import insert_movie, close_connection

# Initialize the bot
app = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
register_start_handler(app)
register_search_handler(app)
register_callback_handler(app)

# Insert sample movies into the database (for testing)
sample_movies = [
    {
        "title": "RRR",
        "year": 2022,
        "language": "Hindi",
        "links": {
            "480p": "https://gplinks.co/y8UZi",
            "720p": "https://gplinks.co/SB45BU",
            "1080p": "https://gplinks.co/A3H2"
        }
    },
    {
        "title": "Come Play",
        "year": 2020,
        "language": "English",
        "links": {
            "480p": "https://example.com/comeplay_480p",
            "720p": "https://example.com/comeplay_720p",
            "1080p": "https://example.com/comeplay_1080p"
        }
    }
]

for movie in sample_movies:
    insert_movie(movie)

# Start the bot
if __name__ == "__main__":
    try:
        print("Bot is running...")
        app.run()
    finally:
        # Close the MongoDB connection when the bot stops
        close_connection()