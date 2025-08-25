import os
from flask import Flask, request
import requests

TOKEN = os.getenv("BOT_TOKEN")  # Add BOT_TOKEN in Render environment
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = "message received wait for reply"

        requests.post(URL, json={
            "chat_id": chat_id,
            "text": text
        })

    return {"ok": True}

# Gunicorn needs "app"
flask_app = app
