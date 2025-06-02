# config.py
import os
from os import environ
import re

# Utility functions
id_pattern = re.compile(r'^-?\d+$')  # Fixed to handle negative integers for channel IDs

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot Information (with validation)
API_ID = environ.get('API_ID', '26954495')
API_HASH = environ.get('API_HASH', '2061c55207cfee4f106ff0dc331fe3d9')
BOT_TOKEN = environ.get('BOT_TOKEN', "")
SESSION = environ.get('SESSION', 'Deendayal_search')

# Validate required environment variables
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set in the environment variables.")

# Bot Settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Admin, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6285713858 7045947967').split()]
DEENDAYAL_MOVIE_UPDATE_CHANNEL = int(environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL', '-1002608186529'))
AUTH_CHANNEL = [int(fch) if id_pattern.search(fch) else fch for fch in environ.get('AUTH_CHANNEL', '-100').split()]

# Channel & Group Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/SDMOVIESPOINTEe')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/pikashow_7')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Keshavraj_77')  # Updated to @Keshavraj_77
DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK = environ.get('DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK', 'https://t.me/pikashow_7')

# MongoDB Configuration
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://nr385708:bs6GdimYoAzmHbRF@cluster0.xtpwl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Deendayal_files')

# Validate MongoDB URI
if not DATABASE_URI:
    raise ValueError("DATABASE_URI must be set in the environment variables.")

# Miscellaneous
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📽️ {file_name}\n\n💾 Size: {file_size}")