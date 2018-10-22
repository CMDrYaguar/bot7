import telebot
bot = telebot.TeleBot("token")
bot.send_message(188966014, "testik")
import random

@bot.message_handler(content_types= ['text'])

def handle_comand(message):
    a = random.randint(1, 4)
    word = message.text
    if (a == 1):
        bot.send_message(message.chat.id, word + "щица")
    elif (a == 2):
        bot.send_message(message.chat.id, word + "тка")
    elif (a == 3):
        bot.send_message(message.chat.id, word + "ша")


bot.polling(none_stop=True, interval=0)
