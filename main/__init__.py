#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int("25164506")
API_HASH = ("2771620a92dd0d044e51a787f18565c0")
BOT_TOKEN = ("6470291664:AAEZTb36MmiNYyRGqPliixsce5EH94byepw")
SESSION = ("BABjxmKpuUjsTZywrQaUn9Dbv-K8S3vNsMBkFHtGD3iD5A33Ehyfh2jv_6Ui0yf_UAM6hmiFGpS805QPcYJwU5yCbKOhrPM6lUsAXeacmyqxlhtHRfP_rOGPQWQ_g9tc9RgdRq9L6Y1CJGC9tok0FXYbhbpcrqNX9lPPhaAoUAO-y2X_4kVqdBYvtW7VBuhBbqmf-yxulQRT4O2ZoYEZGKWisp7e4w_3iIHXQrnbe-cjipvUVW3Hk5DFzo1WPw3jrZyxiL00sIQIgycb15CemQI_HuoJCf6IN1OP3pZj89t05Ijh6V0yLH4h2-cs7j2c4dSMRKvRnJ_JJ3LpqBRXoVKkAAAAAS_eymEA")
FORCESUB = ("Rokubotz")
AUTH = int("5098097249")

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
