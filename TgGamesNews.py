from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv('api_id'))
api_hash = os.getenv('api_hash')

client = TelegramClient("Новости", api_id, api_hash)


@client.on(events.NewMessage(chats=-1003855576691))
async def handler(event):
    await event.forward_to(-1003752567374)


client.start()
client.run_until_disconnected()