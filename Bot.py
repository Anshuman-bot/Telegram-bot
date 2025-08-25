import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# 🔹 FORCE remove webhook
bot.remove_webhook()

@bot.message_handler(func=lambda message: True, content_types=['text'])
def auto_reply(message):
    bot.reply_to(message, "message received and wait for reply")

print("✅ Bot is running on Render...")
bot.infinity_polling()
