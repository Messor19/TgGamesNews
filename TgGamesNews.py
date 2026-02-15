from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
MY_CHANNEL = os.getenv('MY_CHANNEL')
CHANNELS = os.getenv('CHANNELS')

client = TelegramClient("Новости", API_ID, API_HASH)


@client.on(events.NewMessage(CHANNELS))
async def handler(event):
    await event.forward_to(MY_CHANNEL)


client.start()
client.run_until_disconnected()