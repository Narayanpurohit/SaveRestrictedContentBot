#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=26847865, cast=int)
API_HASH = config("API_HASH", default="0ef9fdd3e5f1ed49d4eb918a07b8e5d6")
BOT_TOKEN = config("BOT_TOKEN", default="7782443871:AAEC3CMt6JU_6-ZIFXSVhrUcwIRf_ztHBuY")
SESSION = config("SESSION", default="BAGZqnkAt5U5V5U6bxU-TLQPao-0T8kFLhIvgZT_5uDKo3pStQjpgzyW93UgBDPiyozY0uafKGXHtxN8W3E8HFDUlyQqiRTQjFyW2zuYBrD-aV0rT5PCzMd3vEIqWWEVNS5ricJ_jRLhVuxt1pBw0oSVkOCcd4AqAO_DbMip6h5zigvz7Af9U48LgNX9c8ZeajOBTrzgMh722sCdbSXsd-Ag1o8qxicDMHIAwT8Eqeyalh9FLA5pudiQ88oR4mFhThgjUw7If6hCF7LUbksmwDTxb6RDU-Fp6o4Dq_6f8c9WCcQWuZjsbt0QZRNMLuvKKQCeLIBPlUtiAOs9hHEoP0WHA1MbKgAAAAGUqifiAA")
FORCESUB = config("FORCESUB", default=jn_bots)
AUTH = config("AUTH", default=6789146594, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
