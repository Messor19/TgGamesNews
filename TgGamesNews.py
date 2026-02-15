from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
MY_CHANNEL = int(os.getenv('MY_CHANNEL'))
CHANNELS = os.getenv('CHANNELS').split(',')

for i in range(len(CHANNELS)):
    CHANNELS[i] = int(CHANNELS[i])

client = TelegramClient("Новости", API_ID, API_HASH)

@client.on(events.NewMessage(CHANNELS))
async def handler(event):
    await event.forward_to(MY_CHANNEL)

client.start()
client.run_until_disconnected()