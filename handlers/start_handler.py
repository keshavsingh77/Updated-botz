# handlers/start_handler.py
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHNL_LNK, GRP_LNK

def register_start_handler(app):
    @app.on_message(filters.command("start"))
    async def start(client, message):
        welcome_text = (
            "HEY! OWNER 😍,\n\n"
            "ME! SHAREDISK MOVIE SEARCH BOT 🤖\n\n"
            "I CAN SEARCH MOVIES FOR YOU. 🔍\n\n"
            "MADE WITH ❤️ BY @Keshavraj_77"  # Updated from @ROYALKRISHNA
        )
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("OUR CHANNEL", url=CHNL_LNK),
                    InlineKeyboardButton("OUR GROUP", url=GRP_LNK),
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                ]
            ]
        )
        await message.reply_text(welcome_text, reply_markup=buttons)