import os
from flask import Flask, request
from telegram import Bot, Update

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    
    if update.message:
        chat_id = update.message.chat.id
        bot.send_message(chat_id=chat_id, text="Message received, wait for reply ✅")
    
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
