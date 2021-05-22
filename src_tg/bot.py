import telebot
import keys
from telebot import types
import bot_db
from emoji import emojize

# ------------------telebot
bot = telebot.TeleBot(keys.token)
# ------------------LANG
lang_flag = 0
lang = {"think_ru": "данные записаны", "think_us": "data recorded", "what_us": "What you need to do?","what_ru": "Что мне сделать?" }
# ------------------
flag = 1
def lang_keyboard():
    keyboard_lang = telebot.types.ReplyKeyboardMarkup()
    item_us = types.KeyboardButton(f'🇺🇸')
    item_ru = types.KeyboardButton(f'🇷🇺')
    keyboard_lang.add(item_ru,item_us)
    return keyboard_lang
def main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    item_help = types.KeyboardButton('Помощь')
    item_meeting = types.KeyboardButton('Переговорка')
    item_activity = types.KeyboardButton('Мероприятия')
    item_contact = types.KeyboardButton('Контакты')
    keyboard.add(item_help,item_activity, item_meeting, item_contact)
    return keyboard

def us_main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup()
    item_help = types.KeyboardButton('Help')
    item_meeting = types.KeyboardButton('Meeting room')
    item_activity = types.KeyboardButton('Events')
    item_contact = types.KeyboardButton('Contacts')
    keyboard.add(item_help,item_activity, item_meeting, item_contact)
    return keyboard

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
    if flag == 0:
        if  message.text == '🇺🇸':
            lang_flag = 0
        else:
            lang_flag = 1
        bot.send_message(message.chat.id, f"ok")
        id = bot_db.bot_cheak_user(message.from_user.username)
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
    if flag == 1:
        if message.text == 'Events' or message.text == 'Мероприятия':
            i = 0
            info_len = bot_db.event_len()
            while i < info_len:
                bot.send_message(message.chat.id, bot_db.event(i))
                i+=1


# db = db()
print("all run")
bot.polling()
