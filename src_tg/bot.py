import telebot
import keys
from telebot import types
import bot_db
import random
from emoji import emojize

# ------------------telebot
bot = telebot.TeleBot(keys.token)
# ------------------LANG
lang_flag = 0
pwd_flag = 0
lang = {"think_ru": "данные записаны", "think_us": "data recorded", "what_us": "What you need to do?","what_ru": "Что мне сделать?",
        "help_ru":"Используйте опции на клавиатуре для получения инофрмации. \nдля создания записей используйте приложение",
        "help_us":"Use the options on the keyboard to get information. \nto create records, use the app",
        "no_com_ru":"такой команды нет", "no_com_us":"there is no such command" }
# ------------------
flag = 1
def lang_keyboard():
    keyboard_lang = telebot.types.ReplyKeyboardMarkup()
    item_us = types.KeyboardButton(f'🇺🇸')
    item_ru = types.KeyboardButton(f'🇷🇺')
    keyboard_lang.add(item_ru,item_us)
    return keyboard_lang

def pwd_keyboard_us():
    keyboard_pwd = telebot.types.ReplyKeyboardMarkup()
    item_one= types.KeyboardButton("generated password")
    item_two = types.KeyboardButton("Write your own")
    keyboard_pwd.add(item_one,item_two)
    return keyboard_pwd

def pwd_keyboard_ru():
    keyboard_pwd = telebot.types.ReplyKeyboardMarkup()
    item_one= types.KeyboardButton("Сгенерировать пароль")
    item_two = types.KeyboardButton("Написать свой")
    keyboard_pwd.add(item_one,item_two)
    return keyboard_pwd
def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    item_help = types.KeyboardButton('Помощь')
    item_meeting = types.KeyboardButton('Задачи')
    item_activity = types.KeyboardButton('Мероприятия')
    item_contact = types.KeyboardButton('Контакты')
    item_pwd = types.KeyboardButton('восстановление пароля')
    keyboard.add(item_help,item_activity, item_meeting, item_contact,item_pwd)
    return keyboard

def us_main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    item_help = types.KeyboardButton('Help')
    item_meeting = types.KeyboardButton('Task')
    item_activity = types.KeyboardButton('Events')
    item_contact = types.KeyboardButton('Contacts')
    item_pwd = types.KeyboardButton('recover the password')
    keyboard.add(item_help,item_activity, item_meeting, item_contact,item_pwd)
    return keyboard


def generator():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = 1
    length = 8
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        return (password)
# def lanng(str)
#
#     return dict.get(str)

@bot.message_handler(commands=['help', 'start'])  # команды
def command(message):
    global flag
    global lang_flag
    global lang

    if message.text == "/start":
        bot.send_message(message.chat.id, f"Выберите язык", reply_markup=lang_keyboard())
        flag = 0
    if message.text == "/help":
        bot.send_message(message.chat.id, 'help')

@bot.message_handler(content_types=['text'])
def send_text(message):
    global flag
    global lang_flag
    global pwd_flag
    if flag == 0:
        if  message.text == '🇺🇸':
            lang_flag = 0
        else:
            lang_flag = 1
        bot.send_message(message.chat.id, f"ok")
        id = bot_db.bot_cheak_user(message.from_user.username)[1]
        if id == -1:
            if lang_flag == 0:
                bot.send_message(message.chat.id, lang.get("think_us"))
                bot.send_message(message.chat.id, lang.get("what_us"),reply_markup = us_main_keyboard())
            else:
                bot.send_message(message.chat.id, lang.get("think_ru"))
                bot.send_message(message.chat.id, lang.get("what_ru"),reply_markup = main_keyboard())
            bot_db.logup(message.from_user.username, message.from_user.id)
        else:
            if lang_flag == 0:
                bot.send_message(message.chat.id, lang.get("what_us"),reply_markup = us_main_keyboard())
            elif lang_flag == 1:
                bot.send_message(message.chat.id, lang.get("what_ru") ,reply_markup = main_keyboard())
            bot_db.logup(message.from_user.username, message.from_user.id)
        flag = 1

    elif flag == 1:
        if pwd_flag == 1:
            markup = types.ReplyKeyboardRemove(selective=False)
            if message.text == 'Написать свой' or message.text == 'Write your own':
                bot.send_message(message.chat.id, "Какой пароль мне записать?",reply_markup=markup)
                pwd_flag = 2
            if message.text == 'Сгенерировать пароль' or message.text == 'generated password':
                bot.send_message(message.chat.id, generator(), reply_markup = main_keyboard())
                pwd_flag = 0
        elif pwd_flag == 2:
            bot.send_message(message.chat.id, 'ok', reply_markup = main_keyboard())
            pwd_flag = 0
            print(message.text)
        elif message.text == 'восстановление пароля' or message.text == 'recover the password':
            if lang_flag == 0:
                bot.send_message(message.chat.id, 'Do you want to write your own or generate a password?',reply_markup=pwd_keyboard_us())
            else:
                bot.send_message(message.chat.id,
                                 'Вы хотите написать свой или сгенерировать пароль?',reply_markup=pwd_keyboard_ru())
            pwd_flag = 1
        elif message.text == 'Events' or message.text == 'Мероприятия':
            i = 0
            info_len = bot_db.event_len()
            while i < info_len:
                bot.send_message(message.chat.id, bot_db.event(i))
                i+=1
        elif message.text == 'Помощь' or message.text == 'Help':
            if lang_flag == 0:
                bot.send_message(message.chat.id, lang.get("help_us"))
            else:
                bot.send_message(message.chat.id,lang.get("help_ru"))
        elif message.text == 'Задачи' or message.text == 'Task':
            i = 0
            info_len = bot_db.task_len(bot_db.get_id(message.from_user.username))
            while i < info_len:
                bot.send_message(message.chat.id, bot_db.task(i,bot_db.get_id(message.from_user.username)))
                i += 1
        else:
            if lang_flag == 0:
                bot.send_message(message.chat.id, lang.get("no_com_us"))
            else:
                bot.send_message(message.chat.id, lang.get("no_com_ru"))
print("all run")
bot.polling()
