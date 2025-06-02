# handlers/search_handler.py
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from config import DEENDAYAL_MOVIE_UPDATE_CHANNEL, DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK

def register_search_handler(app):
    @app.on_message(filters.text & ~filters.command(["start"]))
    async def search_movie(client, message):
        user_id = message.from_user.id
        movie_query = message.text.strip()

        # Check if the user has joined the update channel
        try:
            await client.get_chat_member(DEENDAYAL_MOVIE_UPDATE_CHANNEL, user_id)
        except UserNotParticipant:
            # Prompt user to join the update channel
            join_text = (
                "HEY! OWNER 😊\n\n"
                "YOU HAVE TO JOIN OUR UPDATES CHANNEL TO USE ME ✅\n\n"
                "CLICK BELLOW BUTTON TO JOIN NOW. 👇"
            )
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍿 UPDATES CHANNEL 🍿", url=DEENDAYAL_MOVIE_UPDATE_CHANNEL_LNK)
                    ]
                ]
            )
            await message.reply_text(join_text, reply_markup=buttons)
            return
        except Exception as e:
            # Handle other potential errors (e.g., bot not being an admin in the channel)
            await message.reply_text(f"Error checking channel membership: {str(e)}\nPlease contact @Keshavraj_77 for assistance.")
            return

        # If the user has joined, provide a clickable link to search for the movie
        search_text = (
            f"CLICK HERE 👇 FOR \"{movie_query}\""
        )
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"🍿 {movie_query.upper()} 🍿\nCLICK ME FOR RESULTS", callback_data=f"search:{movie_query}"),
                ],
                [
                    InlineKeyboardButton("? HOW TO OPEN LINK ?", callback_data="how_to_open"),
                    InlineKeyboardButton("👈 SEARCH HERE 👈", callback_data="search_here"),
                ]
            ]
        )
        await message.reply_text(search_text, reply_markup=buttons)