from telebot import *
from us import *
import time

bot = TeleBot("Your telegram token")


@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id, usd1+usd)
    time.sleep(6)
    send(message)




bot.polling(non_stop=True)
