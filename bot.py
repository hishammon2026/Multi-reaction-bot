import asyncio
import logging
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

# ലോഗ്സ് കാണാൻ
logging.basicConfig(level=logging.INFO)

# --- കോൺഫിഗറേഷൻ ---
API_ID = 28390522
API_HASH = "bb6e4438855b6c9ac8d9f0d999a664c4"
# നീ തന്ന String Session ഇവിടെ നൽകുന്നു
STRING_SESSION = "1BVtsOHABu0yBRAIqb0mCRk5CDnV8GYMDPR6-sUW4qZNEZuFAnAy1ymp0YYwJxKtCEn2fA_5SwtufMsxelHkqY19c2LF_yOCRAX924tRxQAl2oGgeHXXdNuaevk9gGrgyC26CS8oEy9zTFeKxXQqYkQNRA_pZcDD_doBokRtOuPEigyf7i9CXtVYh-H2FsSovh_WkskHw6nBGzAyQNxvuEHwLn2KSGFPbD-FIU9KjDOBYIvTfjzRV1huNfvPkd5X775QQmO61z2abvNZLG27dSKQVvCVREOvx2iqSLxUzREfjx71b6AWzIGAJuPm4QiSYIAuXHYBxzfH4EALyyZ-vA3dOag0u_c8="

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# 50 റിയാക്ഷനുകൾ ഉള്ള ലിസ്റ്റ്
REACTIONS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", 
    "😢", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", 
    "🌚", "⚡️", "🍌", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", 
    "🤓", "👻", "👨‍💻", "👀", "🎃", "💥", "❄️", "🚫", "🏆", "💔", 
    "🤨", "😐", "🌭", "😘", "🆒", "🦄", "🍭", "👾", "💎", "🍋"
]

@client.on(events.NewMessage)
async def reaction_handler(event):
    # പുതിയ മെസ്സേജ് വരുമ്പോൾ
    try:
        for emoji in REACTIONS:
            await client(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                add_to_recent=True,
                reaction=[ReactionEmoji(emoticon=emoji)]
            ))
            # ടെലിഗ്രാം ഫ്ലഡ് തടയാൻ ചെറിയൊരു ഗ്യാപ്പ് (0.05 സെക്കൻഡ്)
            await asyncio.sleep(0.05)
    except Exception as e:
        logging.error(f"Error: {e}")

print("നിന്റെ Telethon UserBot വിജയകരമായി സ്റ്റാർട്ട് ആയിട്ടുണ്ട്! ചാനലിൽ പോസ്റ്റ് ഇട്ടു നോക്കൂ...")
client.start()
client.run_until_disconnected()
