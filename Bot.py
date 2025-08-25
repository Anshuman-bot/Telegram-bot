import os
import threading
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ======================
# Environment Variables
# ======================
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))  # Telegram numeric user ID

# ======================
# Logging
# ======================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ======================
# Telegram Bot Handlers
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("message is received wait for the reply")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    logger.info(f"Message from {user.first_name} (@{user.username}): {text}")

    # Reply to user
    await update.message.reply_text("message is received wait for the reply")

    # Forward to owner
    forward_text = f"📩 Message from {user.first_name} (@{user.username}):\n\n{text}"
    await context.bot.send_message(chat_id=OWNER_ID, text=forward_text)

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

# ======================
# Flask (for Render)
# ======================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Telegram bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# ======================
# Main
# ======================
if __name__ == "__main__":
    # Start Flask server in background
    threading.Thread(target=run_flask).start()

    # Start Telegram bot
    run_bot()
    # Forward to owner
    forward_text = f"📩 Message from {user.first_name} (@{user.username}):\n\n{text}"
    await context.bot.send_message(chat_id=OWNER_ID, text=forward_text)

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

# ======================
# Flask (for Render)
# ======================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Telegram bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)

# ======================
# Main
# ======================
if __name__ == "__main__":
    # Start Flask server in background
    threading.Thread(target=run_flask).start()

    # Start Telegram bot
    run_bot()logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

...

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    logger.info(f"Message from {user.first_name} (@{user.username}): {text}")

    # Reply to user
    await update.message.reply_text("message is received wait for the reply")

    # Forward to owner
    forward_text = f"📩 Message from {user.first_name} (@{user.username}):\n\n{text}"
    await context.bot.send_message(chat_id=OWNER_ID, text=forward_text)
