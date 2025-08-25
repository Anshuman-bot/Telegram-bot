import telebot
import os

# ✅ Get the token from Render Environment Variables
API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# 🔹 Clear any webhook before polling
bot.remove_webhook()

# 🔹 Handle ALL messages (including /start and commands)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def auto_reply(message):
    bot.reply_to(message, "message received and wait for reply")

print("✅ Bot is running on Render...")
bot.infinity_polling()
