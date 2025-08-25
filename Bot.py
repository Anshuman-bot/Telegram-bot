from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN") or "YOUR_BOT_TOKEN"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

# Home route to check if bot is alive
@app.route("/", methods=["GET"])
def home():
    return "Bot is running"

# Webhook route
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Update received:", data, flush=True)  # log in Render

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        reply_text = "Message received and wait for reply"
        requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": reply_text})

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
