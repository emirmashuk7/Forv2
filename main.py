import os
import threading
import asyncio
import logging
import time
from flask import Flask

# Enable logging for both our app and Pyrogram
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Also enable Pyrogram's internal logging to see updates
logging.getLogger("pyrogram").setLevel(logging.INFO)

print("Starting bot setup...")

# Create and set event loop BEFORE importing anything that uses Pyrogram
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
print("Event loop created and set.")

# Now import bot (which imports Pyrogram)
from bot import Bot
print("Bot imported successfully.")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running", 200

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get('PORT', 8000))
    logger.info(f"Starting Flask on port {port}")
    app.run(host='0.0.0.0', port=port)

def heartbeat():
    """Print a message every minute to show the bot is alive."""
    while True:
        logger.info("Bot is still running...")
        time.sleep(60)

def run_bot():
    logger.info("Starting bot...")
    try:
        # Run the bot using the same loop
        loop.run_until_complete(Bot().run())
    except Exception as e:
        logger.error(f"Bot crashed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Start heartbeat thread (daemon so it exits when main thread exits)
    threading.Thread(target=heartbeat, daemon=True).start()
    # Run the bot in the main thread with its loop
    run_bot()
