from pyrogram import Client
from utils.config import api_id, api_hash

app = Client("auto_stars", api_id=api_id, api_hash=api_hash)

app.run()