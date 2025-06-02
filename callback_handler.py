# handlers/callback_handler.py
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import find_movie

def register_callback_handler(app):
    @app.on_callback_query()
    async def callback_query(client, callback_query):
        data = callback_query.data

        if data.startswith("search:"):
            movie_query = data.split(":", 1)[1]
            movie = find_movie(movie_query)

            if movie:
                # Format the movie details with download links
                result_text = (
                    f"{movie['title'].upper()} ({movie['year']}) 🍿\n\n"
                    f"ORIGINAL {movie['language'].upper()} DUBBED 🎙️\n\n"
                    f"ORIGINAL PRINT 📼\n\n"
                    f"480P - {movie['links']['480p']}\n\n"
                    f"720P - {movie['links']['720p']}\n\n"
                    f"1080P - {movie['links']['1080p']}\n\n"
                    f"UPLOADED BY @DUKAN_KA_SAMAN"
                )
                buttons = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("WRONG LAYOUT?", callback_data="wrong_layout")
                        ]
                    ]
                )
                await callback_query.message.edit_text(result_text, reply_markup=buttons)
            else:
                await callback_query.message.edit_text("Movie not found in the database. Please try a different title or contact @Keshavraj_77 for assistance.")

        elif data == "how_to_open":
            await callback_query.message.edit_text("To open the link, simply click on the resolution link (e.g., 480P, 720P, 1080P) to download or stream the movie.")
        elif data == "search_here":
            await callback_query.message.edit_text("Please type the movie name again to search.")
        elif data == "wrong_layout":
            await callback_query.message.edit_text("If the layout is wrong, please contact the bot owner @Keshavraj_77 for assistance.")  # Updated from @ROYALKRISHNA