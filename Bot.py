import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("RENDER_EXTERNAL_URL")  # Render sets this automatically

flask_app = Flask(__name__)
tg_app = Application.builder().token(TOKEN).build()

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message received, wait for reply")

# Reply to all text messages
async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message received, wait for reply")

tg_app.add_handler(CommandHandler("start", start))
tg_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))

# Webhook endpoint
@flask_app.post(f"/webhook/{TOKEN}")
def webhook():
    update = Update.de_json(request.get_json(force=True), tg_app.bot)
    tg_app.update_queue.put_nowait(update)
    return "ok"

@flask_app.get("/")
def home():
    return "Bot is running ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    tg_app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=f"webhook/{TOKEN}",
        webhook_url=f"{URL}/webhook/{TOKEN}"
    )
    flask_app.run(host="0.0.0.0", port=port)
