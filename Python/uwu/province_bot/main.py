import telebot
from telebot import types

bot = telebot.TeleBot("5448953858:AAHSWrMviMR0blsnYM1NOFdyIGrq4TTpLek")


@bot.message_handler(content_types=['text'], commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    bot.send_message(message.chat.id, "Это хуй", reply_markup=markup)


bot.infinity_polling()
