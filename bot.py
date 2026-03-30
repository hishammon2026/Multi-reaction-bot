import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# നിന്റെ API വിവരങ്ങൾ ഇവിടെ നൽകുക
API_ID = 28390522  # Replace with your API ID
API_HASH = "bb6e4438855b6c9ac8d9f0d999a664c4"
BOT_TOKEN = "8406892242:AAFrUFwPUAKZv2QeXAVzHD0Y0ABcsaELsH4"

app = Client("reaction_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# നിനക്ക് വേണ്ട 50 റിയാക്ഷനുകൾ ഈ ലിസ്റ്റിൽ ഇടാം
REACTIONS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "🌚", "⚡️", "🍌", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "⛸", "💥", "❄️", "🚫", "🏆", "💔", "🤨", "😐", "🍓", "🌭", "😘", "🆒", "🦄", "🍭", "👾"
]

@app.on_message(filters.channel | filters.group)
async def send_reaction(client, message: Message):
    try:
        # ഓരോ റിയാക്ഷനും ഓരോന്നായി മെസ്സേജിലേക്ക് അയക്കുന്നു
        for emoji in REACTIONS:
            await client.send_reaction(
                chat_id=message.chat.id,
                message_id=message.id,
                emoji=emoji
            )
            # ടെലിഗ്രാം ഫ്ലഡ് വരാതിരിക്കാൻ ചെറിയൊരു ഗ്യാപ്പ്
            await asyncio.sleep(0.1) 
    except Exception as e:
        print(f"Error: {e}")

print("ബോട്ട് സ്റ്റാർട്ട് ആയിട്ടുണ്ട്...")
app.run()
