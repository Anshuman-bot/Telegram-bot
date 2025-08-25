import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Load bot token from Railway Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message received, wait for reply")

# Reply to all text messages
async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message received, wait for reply")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found! Please set it in Railway Environment Variables.")

    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))

    # Start bot with polling (no port required)
    app.run_polling()

if __name__ == "__main__":
    main()
