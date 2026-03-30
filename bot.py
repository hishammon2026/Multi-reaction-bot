import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# ലോഗ്സ് കാണാൻ (GitHub Actions-ൽ ബോട്ട് എവിടെ എത്തിയെന്ന് അറിയാൻ)
logging.basicConfig(level=logging.INFO)

# നിന്റെ വിവരങ്ങൾ
API_ID = 28390522
API_HASH = "bb6e4438855b6c9ac8d9f0d999a664c4"
BOT_TOKEN = "8406892242:AAFrUFwPUAKZv2QeXAVzHD0Y0ABcsaELsH4"

# ബോട്ട് ക്ലയന്റ് സെറ്റപ്പ്
app = Client(
    "ReactionBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 50 റിയാക്ഷനുകൾ ഉള്ള ലിസ്റ്റ്
REACTIONS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", 
    "😢", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", 
    "🌚", "⚡️", "🍌", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", 
    "🤓", "👻", "👨‍💻", "👀", "🎃", "💥", "❄️", "🚫", "🏆", "💔", 
    "🤨", "😐", "🌭", "😘", "🆒", "🦄", "🍭", "👾", "💎", "🍋"
]

# ബോട്ട് വർക്ക് ആകുന്നുണ്ടോ എന്ന് നോക്കാൻ /start കമാൻഡ്
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        "**ഹലോ ഡെവലപ്പർ!**\n\n"
        "ഞാൻ മൾട്ടി-റിയാക്ഷൻ ബോട്ട് ആണ്. എന്നെ ചാനലിൽ അഡ്മിൻ ആക്കൂ, "
        "എല്ലാ പോസ്റ്റുകൾക്കും ഞാൻ 50 റിയാക്ഷനുകൾ നൽകും! 🔥"
    )

# ചാനലിലോ ഗ്രൂപ്പിലോ മെസ്സേജ് വരുമ്പോൾ റിയാക്ഷൻ നൽകാൻ
@app.on_message(filters.channel | filters.group)
async def auto_reaction(client, message: Message):
    try:
        for emoji in REACTIONS:
            await client.send_reaction(
                chat_id=message.chat.id,
                message_id=message.id,
                emoji=emoji
            )
            # ടെലിഗ്രാം സർവർ ബ്ലോക്ക് ചെയ്യാതിരിക്കാൻ ചെറിയൊരു ഗ്യാപ്പ്
            await asyncio.sleep(0.1)
    except Exception as e:
        logging.error(f"Error: {e}")

# ബോട്ട് റൺ ചെയ്യാൻ
if __name__ == "__main__":
    print("ബോട്ട് സ്റ്റാർട്ട് ആയിട്ടുണ്ട്...")
    app.run()
