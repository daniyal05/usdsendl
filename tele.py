from telebot import *
from us import *
import time

bot = TeleBot("6696351261:AAG0PSLvOmIecXyOAfqQVWdFAf_2QbDeEv4")


@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id, usd1+usd)
    time.sleep(6)
    send(message)




bot.polling(non_stop=True)
