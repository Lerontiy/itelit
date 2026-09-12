import telebot
from telebot import types


search_list = list()
now_speaking_list = list()


def menu_buttons(mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton("Знайти співрозмовника")
    gender = types.KeyboardButton("Шукати по гендеру")
    inter = types.KeyboardButton("Інтереси пошуку")
    markup.add(start, gender, inter)
    return markup


bot = telebot.TeleBot("5366703735:AAFhpT3rLfLw0SoAI0L-lVzXkLWDdUQBj-Y")


@bot.message_handler(content_types=['text'], commands=['start', 'search'])
def start(message):
    search_list.append(message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton("Зупинити пошук співрозмовника")
    markup.add(start)
    bot.send_message(message.chat.id, "<em>Пошук співрозмовника...</em>\n",
                                    parse_mode="html", reply_markup=markup)
    while not len(search_list) > 0:
        pass
    if len(search_list) > 0 and (message.chat.id in search_list):
        if not message.chat.id in now_speaking_list: #and (search_set[0] != message.chat.id):
            now_speaking_list.append([message.chat.id, search_list[0]])
            search_list.remove(message.chat.id)
            a = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Співрозмовник <em>знайдений</em> 🐵\n"
                                                "/next <em>- шукати нового співрозмовника</em>\n"
                                                "/stop <em>- зупинити діалог</em>", parse_mode="html", reply_markup=a)


@bot.message_handler(commands=['stop'])
def stop(message):
    for i in now_speaking_list:
        if message.chat.id in i:
            bot.send_message(message.chat.id, "<em>Ви закінчили розмову з Вашим співрозмовником 🙄</em>\n"
                                           "<em>Напишіть</em> /search <em>щоб знайти наступного</em>",
                             parse_mode="html", reply_markup=menu_buttons(message))
            for j in i:
                if j != message.chat.id:
                    bot.send_message(i[i.index(j)], "<em>Співрозмовник розірвав з Вами зв'язок 😞</em>\n"
                                                    "<em>Напишіть</em> /search <em>щоб знайти наступного</em>", parse_mode="html")
                break
            now_speaking_list.remove(now_speaking_list[now_speaking_list.index(i)])


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "<em>Це бот для анонімного спілкування у Телеграмі\n\n"
                                    "Бот вміє пересилати повідомлення, фото, відео, гіфки, стікери, аудіо та відеоповідомлення.</em>\n\n"
                                    "/search <em>— пошук співрозмовника</em>\n"
                                    "/next <em>— закінчити поточний діалог і одразу ж шукати нового співрозмовника</em>\n"
                                    "/stop <em>— закінчити розмову із співрозмовником</em>\n"
                                    "/interests <em>— вибрати інтереси пошуку</em>\n"
                                    "/link <em>— надіслати співрозмовнику посилання на вас у Телеграмі</em>\n"
                                    "/settings <em>— змінити свою стать та інші налаштування</em>\n"
                                    "/rules <em>— ознайомитись із правилами\n\n</em>", parse_mode="html")


@bot.message_handler(commands=['send_message'])
def send_message_info(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['super'])
def super(message):
    bot.send_message(message.chat.id, "Капуста")


@bot.message_handler()
def send_message(message):
    if message.text == "Знайти співрозмовника":
        start(message)
    elif message.text == "Зупинити пошук співрозмовника":
        if message.chat.id in search_list:
            search_list.remove(message.chat.id)
            bot.send_message(message.chat.id, "<em>Ви завершили пошук співрозмовника 🙄</em>\n"
                                           "<em>Напишіть</em> /search <em>щоб знайти наступного</em>",
                             parse_mode="html", reply_markup=menu_buttons(message))
        else:
            for i in now_speaking_list:
                if message.chat.id in i:
                    bot.send_message(message.chat.id, "<em>У Вас вже є співрозмовник 🤔</em>\n"
                                                      "/next <em>- шукати нового співрозмовника</em>\n"
                                                      "/stop <em>- зупинити діалог</em>", parse_mode="html")
                else:
                    bot.send_message(message.chat.id, "<em>У Вас ще немає співрозмовника 🤔</em>", parse_mode="html")
    else:
        for i in now_speaking_list:
            if message.chat.id in i:
                for j in i:
                    if j != message.chat.id or j == message.chat.id:
                        bot.send_message(i[i.index(j)], message.text)
                    break
            else:
                bot.send_message(message.chat.id, "<em>Напишіть</em> /search <em>для пошуку співрозмовника</em>", parse_mode="html")
            break
        if len(now_speaking_list) == 0:
            bot.send_message(message.chat.id, "<em>Напишіть</em> /search <em>для пошуку співрозмовника</em>", parse_mode="html")


bot.infinity_polling()
