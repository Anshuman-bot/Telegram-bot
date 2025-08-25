import telebot

API_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.reply_to(message, "message received and wait for reply")

print("Bot is running...")
bot.infinity_polling()  # ✅ keep only this
