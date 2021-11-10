from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgQAAxkBAAEBAVBhi-xWk3J4wULennxxK3C2v_VVwgACuwUAAqcgawSuONdA8Q9lQSIE"


START_TEXT = """
👋 Hey {} I am a versatile Automated Bot that can play music in Telegram Group Voice Chats.


🔆Thank you for starting me @luvchaeyoung_robot.

 🔆My developer is @ucant_surpassmebruh 🇱🇰🇰🇷🇯🇵

🔆If you wish to donate, please PM my developer and contact him for any sort of inquiries as well.

⭕️⭕️⭕️⭕️

A sincere request to join our bot updates channel and discussion group using the links 🔗 below;

☯️Discussion :- https://t.me/luvchaeyoung_botupdates

☯️Updates Channel:- https://t.me/RoseannePark_updates

**Commands** [Here]("https://telegra.ph/file/60abc9b21f4378e922e5e.jpg")

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url="https://t.me/RoseannePark_updates"),
        InlineKeyboardButton('Group', url='https://t.me/luvchaeyoung_botupdates')
        ]]
  
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_sticker(STICKER)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )

