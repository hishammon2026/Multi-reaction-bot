import asyncio
import logging
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji
from telethon.errors import FloodWaitError

logging.basicConfig(level=logging.INFO)

# --- കോൺഫിഗറേഷൻ ---
API_ID = 28390522
API_HASH = "bb6e4438855b6c9ac8d9f0d999a664c4"
STRING_SESSION = "1BVtsOHABu0yBRAIqb0mCRk5CDnV8GYMDPR6-sUW4qZNEZuFAnAy1ymp0YYwJxKtCEn2fA_5SwtufMsxelHkqY19c2LF_yOCRAX924tRxQAl2oGgeHXXdNuaevk9gGrgyC26CS8oEy9zTFeKxXQqYkQNRA_pZcDD_doBokRtOuPEigyf7i9CXtVYh-H2FsSovh_WkskHw6nBGzAyQNxvuEHwLn2KSGFPbD-FIU9KjDOBYIvTfjzRV1huNfvPkd5X775QQmO61z2abvNZLG27dSKQVvCVREOvx2iqSLxUzREfjx71b6AWzIGAJuPm4QiSYIAuXHYBxzfH4EALyyZ-vA3dOag0u_c8="

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# കൃത്യം 50 എണ്ണം
REACTIONS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬",
    "😢", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴",
    "🌚", "⚡️", "🍌", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭",
    "🤓", "👻", "👨‍💻", "👀", "🎃", "💥", "❄️", "🚫", "🏆", "💔",
    "🤨", "😐", "🌭", "😘", "🆒", "🦄", "🍭", "👾", "💎", "🍋"
]

@client.on(events.NewMessage)
async def reaction_handler(event):
    if not event.is_channel and not event.is_group:
        return

    print(f"പുതിയ മെസ്സേജ് വന്നു! 50 റിയാക്ഷനുകൾ തുടങ്ങുന്നു...")
    
    for emoji in REACTIONS:
        try:
            await client(SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                add_to_recent=True,
                reaction=[ReactionEmoji(emoticon=emoji)]
            ))
            # 1.5 സെക്കൻഡ് കാത്തിരിക്കണം, ഇല്ലെങ്കിൽ വീണ്ടും ബ്ലോക്ക് കിട്ടും
            await asyncio.sleep(1.5)
            
        except FloodWaitError as e:
            print(f"ടെലിഗ്രാം നമ്മളെ തടഞ്ഞു! {e.seconds} സെക്കൻഡ് കാത്തിരിക്കുന്നു...")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Error: {e}")
            continue

print("നിന്റെ 50 Reaction ബോട്ട് ഓടാൻ തയ്യാറാണ്!")
client.start()
client.run_until_disconnected()
