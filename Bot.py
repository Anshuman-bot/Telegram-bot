import os
import ssl
import certifi
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

# ---------------- Flask App ----------------
app = Flask(__name__)

# ---------------- Telegram Bot Setup ----------------
TOKEN = os.getenv("BOT_TOKEN")  # Set in Render Environment Variables

# Force HTTPS with certifi
request = HTTPXRequest(ssl_context=ssl.create_default_context(cafile=certifi.where()))

# Create application
application = Application.builder().token(TOKEN).request(request).build()

# ---------------- Handlers ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is up and running on Render!")

application.add_handler(CommandHandler("start", start))

# ---------------- Flask Webhook Route ----------------
@app.route("/webhook", methods=["POST"])
async def webhook():
    """Receive updates from Telegram and feed them to PTB"""
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok", 200

@app.route("/")
def home():
    return "🤖 Bot is running!", 200

# ---------------- Run ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Set webhook (only once when container starts)
    import asyncio
    async def set_webhook():
        url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/webhook"
        await application.bot.set_webhook(url)
    asyncio.run(set_webhook())

    app.run(host="0.0.0.0", port=port)
