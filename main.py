import os
import threading
import asyncio
from flask import Flask

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
    print(f"Starting Flask on port {port}")
    app.run(host='0.0.0.0', port=port)

def run_bot():
    print("Starting bot...")
    try:
        # Run the bot using the same loop
        loop.run_until_complete(Bot().run())
    except Exception as e:
        print(f"Bot crashed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()
    # Run the bot in the main thread with its loop
    run_bot()
