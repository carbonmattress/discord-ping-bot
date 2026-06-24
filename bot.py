import os
import discord
import requests

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TRIGGER_WORDS = ["hi", "hey", "hello"]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content.lower().split() for word in TRIGGER_WORDS):
        payload = {
            "content": f"<@{message.author.id}>, you said a trigger word!"
        }
        requests.post(WEBHOOK_URL, json=payload)

client.run(BOT_TOKEN)
