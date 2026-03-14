import os
import threading
import asyncio
from flask import Flask

# 1. Create and set event loop BEFORE importing anything that uses Pyrogram
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# 2. Now import bot (which imports Pyrogram)
from bot import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running", 200

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    # Run the bot using the same loop
    loop.run_until_complete(Bot().run())  # use .run() if .run is async

if __name__ == '__main__':
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Run the bot in the main thread with its loop
    run_bot()
