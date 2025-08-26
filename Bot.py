from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Get the bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Simple response
    if text.lower() == "hi":
        bot.sendMessage(chat_id=chat_id, text="Hello 👋, I'm alive on Render!")
    else:
        bot.sendMessage(chat_id=chat_id, text=f"You said: {text}")

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
