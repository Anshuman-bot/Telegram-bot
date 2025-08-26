import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from PIL import Image

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

# --- Handlers ---
def start(update, context):
    update.message.reply_text("Hello! I am alive 🚀")

def handle_message(update, context):
    update.message.reply_text("Message received, wait for reply ✅")

def handle_photo(update, context):
    file = context.bot.getFile(update.message.photo[-1].file_id)
    file_path = "temp.jpg"
    file.download(file_path)

    if is_image(file_path):
        update.message.reply_text("✅ This looks like an image!")
    else:
        update.message.reply_text("⚠️ File is not a valid image.")

    os.remove(file_path)

def is_image(path):
    try:
        Image.open(path)
        return True
    except:
        return False

# --- Dispatcher setup ---
dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))

# --- Flask routes ---
@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"
