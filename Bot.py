import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # use environment variable
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.reply_to(message, "Hello! This is an auto-reply 🤖 (running on Render)")

print("Bot is running...")
bot.infinity_polling()
