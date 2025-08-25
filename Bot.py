import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv("BOT_TOKEN")  # set this in Render → Environment
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# ✅ Reply to ALL messages (even /start)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def auto_reply(message):
    bot.reply_to(message, "message received and wait for reply")

# ✅ Telegram will POST updates here
@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# ✅ Just to test if service is alive
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    # Remove any old webhook & set new one to your Render URL
    bot.remove_webhook()
    render_url = f"https://YOUR-RENDER-APP.onrender.com/{API_TOKEN}"
    bot.set_webhook(url=render_url)

    # Run Flask app on Render-assigned port
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
