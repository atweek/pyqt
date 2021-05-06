import telebot
import keys
# from telebot import types
# from emoji import emojize

# ------------------telebot
bot = telebot.TeleBot(keys.token)
# ------------------БД
#db
# ------------------

# def main_keyboard():
#     keyboard2 = telebot.types.ReplyKeyboardMarkup()
#     item_help = types.KeyboardButton('Помощь')
#     item_vacation = types.KeyboardButton('Отпуск')
#     item_cash = types.KeyboardButton('Когда зарплата?')  # -------------------------!
#     item_wifi = types.KeyboardButton('wi-fi')
#     item_job = types.KeyboardButton('Когда на работу?')
#     item_meeting = types.KeyboardButton('Переговорка')
#     item_activity = types.KeyboardButton('Мероприятия')
#     item_contact = types.KeyboardButton('Контакты')
#     item_doc = types.KeyboardButton('Заказать документ')
#     item_pass = types.KeyboardButton('Заказать пропуск гостю')
#     keyboard2.add(item_help, item_vacation, item_wifi, item_cash, item_activity, item_meeting, item_job, item_contact,
#                   item_doc, item_pass)
#     return keyboard2


@bot.message_handler(commands=['help', 'start'])  # команды
def command(message):
    global help_flag
    if message.text == "/start":
        t_id = str(message.chat.id)
        bot.send_message(message.chat.id, 'Привет')
    if message.text == "/help":
        bot.send_message(message.chat.id, 'help')


# @bot.message_handler(content_types=['text'])  # текст
# def send_text(message):
#     global full_name
#     global flag
#     global wifi_in
#     global doc_flag
#     global id
#     global help_flag
#     global get_doc_flag
#     global pass_flag
#     if message.text.lower() == 'помощь':
#         bot.send_message(message.chat.id, help)
#         help_flag = 1
#     elif message.text.lower() == 'учитель':
#         help_flag = 0
#         if type(message.chat.id) == "":
#             if flag == 0:
#                 flag = 11
#                 keyboard1 = telebot.types.ReplyKeyboardMarkup()
#                 item_help = types.KeyboardButton('Помощь')
#                 keyboard1.row(item_help)
#                 bot.send_message(message.chat.id, 'Введите ваш id', reply_markup=keyboard1)
#
#         else:
#             bot.send_message(message.chat.id, unrecognized)
#     elif flag == 11:
#         help_flag = 0
#         id = message.text
#         cursor = con.cursor()
#         cursor.execute(f"SELECT name FROM teacher WHERE id = '{message.text}'")
#         bot.send_message(message.chat.id, "Здравствуйте " + str(cursor.fetchone())[2:-3])
#         cursor.close()
#         bot.send_message(message.chat.id, "ВВедите ваш пароль")
#         flag = 12
#     elif help_flag == 1:  # __________________________________________________________________________
#         help_flag = 0
#         bot.send_message(1229152302,
#                          f"Запрос от {message.chat.first_name} {message.chat.last_name} ({message.chat.username})\nЗапрос:{message.text}")
#         help_flag = 2
#         id = message.chat.id
#     elif help_flag == 2:  # ___________________________________________________________________________
#         help_flag = 0
#         bot.send_message(id, f"Ответ на запрос: {message.text}")
#         help_flag = 0
#     # elif flag == 21:
#     #     id = message.text
#     #     cursor = con.cursor()
#     #     cursor.execute(f"SELECT full_name FROM student WHERE id = '{message.text}'")
#     #     bot.send_message(message.chat.id,"Здравствуйте " + str(cursor.fetchone())[2:-3])
#     #     cursor.close()
#     #     bot.send_message(message.chat.id,"ВВедите ваш пароль")
#     #     flag=22
#     elif flag == 12:
#         cursor = con.cursor()
#         cursor.execute("SELECT password FROM teacher WHERE id =" + id)
#         password = str(cursor.fetchone())[2:-3]
#         cursor.close()
#         if message.text == password:
#             bot.send_message(message.chat.id, "Вы авторизованы", reply_markup=main_keyboard())
#             cursor = con.cursor()
#             cursor.execute(
#                 "UPDATE teacher SET telegram_id = " + str(message.chat.id) + " ,activity = '1' WHERE id=" + id)
#             con.commit()
#             cursor.close()
#             flag = 13
#         else:
#             bot.send_message(message.chat.id, "пароль не правильный!")
#             flag = 12
#     # elif flag == 22:
#     #     help_flag = 0
#     #     cursor = con.cursor()
#     #     cursor.execute("SELECT password FROM student WHERE id =" + id)
#     #     password = str(cursor.fetchone())[2:-3]
#     #     cursor.close()
#     #     if message.text == password:
#     #         bot.send_message(message.chat.id, "Вы авторизованы",reply_markup=st_keyboard())
#     #         cursor = con.cursor()
#     #         cursor.execute("UPDATE student SET telegram_id = "+str(message.chat.id)+ " ,activity = '1' WHERE id=" + id)
#     #         con.commit()
#     #         cursor.close()
#     #         flag =23
#     #     else:
#     #         bot.send_message(message.chat.id,"пароль не правильный!")
#     #         flag = 12
#     elif type(message.chat.id) == "teacher":  # Функционал для зарегестрированого преподователя
#         help_flag = 0
#         cursor = con.cursor()
#         cursor.execute("SELECT name FROM teacher WHERE telegram_id = '" + str(message.chat.id) + "';")
#         name = str(cursor.fetchone())[2:-3]
#         if message.text.lower() == 'отпуск':
#             help_flag = 0
#             cursor = con.cursor()
#             cursor.execute("SELECT vacation_stay FROM teacher WHERE telegram_id = '" + str(message.chat.id) + "';")
#             bot.send_message(message.chat.id, emojize(
#                 f"Осталось " + str(plural_days(int(str(cursor.fetchone())[1:-2]))) + "  отпуска :beach_with_umbrella:",
#                 use_aliases=True))
#             cursor.close()
#         elif message.text.lower() == "контакты":
#             help_flag = 0
#             global cont_flag
#             bot.send_message(message.chat.id, "Кого вы хотите найти ?\nВведите Фамилию и Имя")
#             cont_flag = 1
#         elif message.text.lower() == "переговорка":
#             help_flag = 0
#             global meet_falag
#             print(str(time.asctime())[11:-8])
#             bot.send_message(message.chat.id, "Во сколько она вам нужна ?\nНапример:17:00")
#             meet_falag = 1
#
#         elif message.text.lower() == "мероприятия":
#             help_flag = 0
#             cursor = con.cursor()
#             cursor.execute("SELECT place,time,contingent,comment,date FROM activity;")
#             select = cursor.fetchall()
#             print(select)
#             for i in range(len(select)):
#                 if select[i][2] == "t":
#                     contingent = "для преподователей"
#                 else:
#                     contingent = f"Для студентов {select[i][2]} курса"
#                 bot.send_message(message.chat.id,
#                                  f"{select[i][3]} \nМесто: {select[i][0]} \nв {select[i][1]} {select[i][4]} \n{contingent}")
#             cursor.close()
#         elif message.text.lower() == "когда на работу?":
#             help_flag = 0
#
#             week_today = datetime.date.weekday(datetime.date.today())
#             cursor = con.cursor()
#             cursor.execute(f"SELECT work_days FROM teacher WHERE telegram_id = '{message.chat.id}'")
#             job_array = str(cursor.fetchone())[2:-3].split(" ")
#             print(job_array)
#             try:
#                 job_tomorrow = job_array[week_today + 1]
#                 print(1)
#             except:
#                 job_tomorrow = job_array[0]
#                 print(2)
#
#             print(job_tomorrow)
#             if job_tomorrow == "0":
#                 help_flag = 0
#                 bot.send_message(message.chat.id, emojize(f"Завтра у вас выходной! :house:", use_aliases=True))
#                 rest = str(int(job_array.index("1")) - int(week_today))
#                 if int(rest) < 0:
#                     rest = str(len(job_array) - (int(week_today) - int(job_array.index("1"))))
#
#                 bot.send_message(message.chat.id, f"На работу через {plural_days(job_array.index('1'))}")
#             if job_tomorrow == "1":
#                 bot.send_message(message.chat.id, emojize(f"Завтра на работу! :man_teacher: ", use_aliases=True))
#             cursor.close()
#         elif message.text.lower() == 'когда зарплата?':
#             cursor = con.cursor()
#             cursor.execute("SELECT payday FROM teacher WHERE telegram_id = '" + str(message.chat.id) + "';")
#             payday = str(cursor.fetchone())[1:-2]
#             cursor.close()
#             cursor = con.cursor()
#             cursor.execute("SELECT advance_day FROM teacher WHERE telegram_id = '" + str(message.chat.id) + "';")
#             advance_day = str(cursor.fetchone())[1:-2]
#             cursor.close()
#             if day_today() >= int(payday):
#                 bot.send_message(message.chat.id,
#                                  emojize("Вы уже должны были все получить! :money_with_wings:", use_aliases=True))
#             elif day_today() < int(advance_day):
#                 bot.send_message(message.chat.id, emojize(
#                     "До аванса осталось " + str(plural_days(int(advance_day) - day_today())) + " :money_bag:",
#                     use_aliases=True))
#                 bot.send_message(message.chat.id, emojize("До заработной платы осталось " + str(
#                     plural_days(int(payday) - day_today())) + "  :money-mouth_face:", use_aliases=True))
#             else:
#                 bot.send_message(message.chat.id, emojize("До заработной платы осталось " + str(
#                     plural_days(int(payday) - day_today())) + "  :money-mouth_face:", use_aliases=True))
#         elif message.text.lower() == 'заказать документ':
#             bot.send_message(message.chat.id, "Какой документ вам нужен?")
#             get_doc_flag = 1
#         elif get_doc_flag == 1:
#             bot.send_message(message.chat.id, "Направлено вашему руководителю")
#             bot.send_message(1229152302,
#                              f"Пользователь {message.chat.first_name} {message.chat.last_name} запросил документ '{message.text}'")
#             get_doc_flag = 0
#
#         elif message.text.lower() == 'wi-fi':
#             if wifi_in == 0:
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 item1 = types.InlineKeyboardButton("ПО", callback_data="po")
#                 item2 = types.InlineKeyboardButton("ОУИТ", callback_data="oyit")
#                 item3 = types.InlineKeyboardButton("ОГРБ", callback_data="ogrb")
#                 markup.add(item1, item2, item3)
#                 bot.send_message(message.chat.id, 'В каком вы отдеоение ?', reply_markup=markup)
#         elif message.text.lower() == 'заказать пропуск гостю':
#             bot.send_message(message.chat.id, "Для кого(ФИО)?")
#             pass_flag = 1
#         elif pass_flag == 1:
#             bot.send_message(message.chat.id, "Причина посещения?")
#             full_name = message.text
#             pass_flag = 2
#         elif pass_flag == 2:
#
#             desc = message.text
#             bot.send_message(1229152302,
#                              f"{message.chat.last_name} {message.chat.first_name} запросил пропуск для гостя {full_name}\nПричина: '{desc}'")
#             bot.send_message(message.chat.id, "Отправлено")
#             pass_flag == 0
#         elif cont_flag == 1:
#             try:
#                 name = message.text.split(" ")
#                 print(name)
#                 cursor = con.cursor()
#                 print(name[0])
#                 cursor.execute(
#                     f"SELECT email,phone_number FROM teacher WHERE surname = '{name[0]}' and name = '{name[1]}'")
#                 contact = cursor.fetchone()
#                 print(contact)
#                 bot.send_message(message.chat.id, f"email: {contact[0]}\nтелефон: {contact[1]}")
#             except:
#                 bot.send_message(message.chat.id, "Не найдено")
#             cont_flag = 0
#         elif wifi_in == 1:
#             cursor = con.cursor()
#             cursor.execute(
#                 f"SELECT name FROM wifi_password WHERE branch = '{wifi_place}' AND auditory = '{message.text.lower().strip()}'")
#             name_wifi = cursor.fetchone()
#             cursor.close()
#             cursor = con.cursor()
#             cursor.execute(
#                 f"SELECT password FROM wifi_password WHERE branch = '{wifi_place}' AND auditory = '{message.text.lower().strip()}'")
#             password_wifi = cursor.fetchone()
#             cursor.close()
#             wifi_in = 0
#             print(name_wifi)
#             print(password_wifi)
#             if name_wifi == None and password_wifi == None:
#                 bot.send_message(message.chat.id, "Аудитория не найдена!", reply_markup=main_keyboard())
#             else:
#                 bot.send_message(message.chat.id, f"Название: {str(name_wifi)[2:-3]}", reply_markup=main_keyboard())
#                 bot.send_message(message.chat.id, f"Пароль: {str(password_wifi)[2:-3]}", reply_markup=main_keyboard())
#         elif doc_flag == 1:
#             global doc_id
#             full_name = message.text.lower()
#             cursor = con.cursor()
#             full_name = full_name.split(" ")
#             print(full_name)
#             try:
#                 cursor.execute(
#                     f"SELECT telegram_id FROM teacher WHERE surname = '{full_name[0].capitalize()}' AND name='{full_name[1].capitalize()}';")
#                 out_id = cursor.fetchone()
#                 print(out_id)
#                 cursor.close()
#                 cursor = con.cursor()
#                 cursor.execute(f"SELECT surname,name FROM teacher WHERE telegram_id = '{message.chat.id}';")
#                 surname_out = cursor.fetchone()
#                 bot.send_message(str(out_id)[2:-3], f"Вам пришел документ от {surname_out[0]} {surname_out[1]}")
#                 bot.send_document(str(out_id)[2:-3], doc_id)
#                 doc_flag = 0
#                 cursor.close()
#             except:
#                 doc_flag = 0
#                 bot.send_message(message.chat.id, "Не найдено!")
#         elif meet_falag == 1:
#             global start_meet
#             start_meet = message.text
#             bot.send_message(message.chat.id, "Во сколько вы закончите ?")
#             meet_falag = 2
#         elif meet_falag == 2:
#             try:
#                 end_meet = int(message.text[0:2] + message.text[3:])
#                 start_meet = int(start_meet[0:2] + start_meet[3:])
#                 print(start_meet)
#                 print(end_meet)
#                 meet_falag = 0
#                 cursor = con.cursor()
#                 cursor.execute(f"SELECT time_start,time_end FROM meeting_room;")
#                 fetch = cursor.fetchall()
#                 print(fetch)
#                 key = 0
#                 for i in range(len(fetch)):
#                     start = int(str(fetch[i][0])[0:2] + str(fetch[i][0])[3:])
#                     end = int(str(fetch[i][1])[0:2] + str(fetch[i][1])[3:])
#                     print(start)
#                     print(end)
#                     if not (start_meet < start and end_meet <= start or start_meet > end and end_meet < start):
#                         break
#                 else:
#                     key = 1
#
#                 if key == 1:
#                     bot.send_message(message.chat.id, "переговорка закрепленна за вами!")
#                 else:
#                     bot.send_message(message.chat.id, "К сожалению время занято !")
#
#                 print(key)
#             except:
#                 bot.send_message(message.chat.id, "Кажется вы ошиблись")
#
#
#
#
#         else:
#             bot.send_message(message.chat.id, 'В разработке!2')
#     # elif type(message.chat.id) == "student":# Функционал для зарегестрированого Студента
#     #     if message.text.lower() =='расписание':
#     #         bot.send_document(message.chat.id, "https://collegetsaritsyno.mskobr.ru/attach_files/upload_users_files/5ea2e9c76e3f5.pdf")
#     #     elif message.text.lower() == 'расписание звонков':
#     #          bot.send_document(message.chat.id, "https://collegetsaritsyno.mskobr.ru/attach_files/upload_users_files/5d695fdd2cc3a.pdf")
#     #
#     # else:
#     #     bot.send_message(message.chat.id,unrecognized)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     global wifi_in
#     if call.message:
#         global wifi_place
#         wifi_place = call.data
#         wifi_in = 1
#         keyboard3 = telebot.types.ReplyKeyboardMarkup()
#         keyboard3.add(types.KeyboardButton("Холл"), types.KeyboardButton("конференц-зал"))
#         bot.send_message(call.message.chat.id, 'Выберите название или введите № кабинета', reply_markup=keyboard3)
#
#
# @bot.message_handler(content_types=['document'])
# def handle_file(message):
#     global doc_flag
#     global doc_id
#     bot.send_message(message.chat.id, 'Напишите фамилию и имя получателя \nНапример:Потапов Ридван')
#     doc_id = message.document.file_id
#     doc_flag = 1
#

print("all run")
bot.polling()
