import os
import discord
import requests
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TRIGGER_WORDS = ["hi", "hey", "hello", "nga", "superforce", "alfusa", "bitch", "aifusa", "nija", "captain", "greetings", "salutations", "retard", "noob", "zyy", "67", "fuck", "fack", "dick", "shit", "clanker", "femboy", "goth", "twink", "phonk", "furry"]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content.lower().split() for word in TRIGGER_WORDS):
        payload = {"content": "<@883772450586918943> superforce sucks"}
        requests.post(WEBHOOK_URL, json=payload)

Thread(target=run_web_server).start()
client.run(BOT_TOKEN)
