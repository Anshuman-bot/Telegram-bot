import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Dispatcher to handle updates
dispatcher = Dispatcher(bot, None, workers=0)

# Function to reply to all messages
def reply_message(update, context):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text="Message received, wait for reply ✅")

# Add handler
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))
dispatcher.add_handler(MessageHandler(Filters.command, reply_message))

@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
