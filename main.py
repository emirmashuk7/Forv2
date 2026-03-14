import os
import threading
import asyncio
from flask import Flask
from bot import Bot

# Create and set an event loop for the main thread
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

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
    # Run the bot using the existing loop
    loop.run_until_complete(Bot().start())
    # If Bot().run() is blocking, you might need loop.run_forever()
    # But let's try this first.

if __name__ == '__main__':
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Run the bot in the main thread with its loop
    run_bot()
