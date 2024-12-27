import os
import telebot

# خواندن توکن از متغیر محیطی
TOKEN = os.getenv('TELEGRAM_TOKEN')

# چک کردن اینکه آیا توکن به درستی از متغیر محیطی دریافت شده یا نه
if not TOKEN:
    raise ValueError("توکن ربات وارد نشده است!")

# ساخت ربات با استفاده از توکن
bot = telebot.TeleBot(TOKEN)

# تعریف تابع برای ارسال پیام
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من ربات شما هستم.")

# شروع ربات و انجام عملیات polling
bot.polling()

