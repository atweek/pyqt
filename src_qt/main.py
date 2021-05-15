# from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from disigner.login import Ui_Dialog as Ui_Auth
from disigner.mainwin import Ui_Dialog as Ui_MAIN
from disigner.singup import Ui_Dialog as Ui_LOGUP
from disigner.tg_warning import Ui_Dialog as Ui_Tg_Warning
from db import db
#pyuic5 test.ui -o test.py -x



class logup_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(logup_win, self).__init__()
        self.ui = Ui_LOGUP()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.name.setPlaceholderText(" введите логин")
        self.ui.email.setPlaceholderText(" введите email")
        self.ui.tg.setPlaceholderText(" введите telegram login")
        self.ui.pwd.setPlaceholderText(" введите пароль")
        self.ui.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.phone.setPlaceholderText(" введите номер телефона")
        self.ui.signup.clicked.connect(self.check_info)
        self.ui.lognin.clicked.connect(self.login)
        self.hide_w()
    def login(self):
        self.destroy()
        self.application = Auth()
        self.application.show()
    def hide_w(self):
        self.ui.emailw.hide()
        self.ui.phomew.hide()
        self.ui.pwdw.hide()
        self.ui.tgw.hide()
        self.ui.emailw_2.hide()
    def check_info(self):
        self.hide_w()
        flag = 0
        if (self.ui.name.text() == ""):
            self.ui.emailw_2.show()
            flag = 1
        if (self.ui.email.text() == ""):
            self.ui.emailw.show()
            flag = 1
        if (self.ui.pwd.text() == ""):
            self.ui.pwdw.show()
            flag = 1
        if (self.ui.tg.text() == ""):
            self.ui.tgw.show()
            flag = 1
        if (self.ui.phone.text() == ""):
            self.ui.phomew.show()
            flag = 1
        if (flag == 0):
            db.logup(self.ui.name.text(), self.ui.pwd.text(), self.ui.phone.text(), self.ui.email.text(), self.ui.tg.text())
            self.destroy()
            self.application = Auth()
            self.application.show()

    def init_UI(self):
        self.setWindowTitle("diplome")

class main_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_win, self).__init__()
        self.ui = Ui_MAIN()
        self.ui.setupUi(self)
        self.init_UI()
        # db.check_events()
        self.init_events()
        self.off_task()
        self.on_task()
        self.init_task()
    def init_task(self):
        self.count_t = db.count_task()
        info = db.check_tasks()
        print(info)

    def on_task(self):
        self.count_t = db.count_task()
        if (self.count_t > 0):
            self.ui.task_1.show()
        if (self.count_t > 1):
            self.ui.task_2.show()
        if (self.count_t > 2):
            self.ui.task_3.show()
        if (self.count_t > 3):
            self.ui.task_4.show()
        if (self.count_t > 4):
            self.ui.task_5.show()
        if (self.count_t > 5):
            self.ui.task_6.show()
        if (self.count_t > 6):
            self.ui.task_7.show()
        if (self.count_t > 7):
            self.ui.task_8.show()
        if (self.count_t > 8):
            self.ui.task_9.show()
        if (self.count_t > 9):
            self.ui.task_10.show()
    def off_task(self):
        self.ui.task_1.hide()
        self.ui.task_2.hide()
        self.ui.task_3.hide()
        self.ui.task_4.hide()
        self.ui.task_5.hide()
        self.ui.task_6.hide()
        self.ui.task_7.hide()
        self.ui.task_8.hide()
        self.ui.task_9.hide()
        self.ui.task_10.hide()



    def init_events(self):
        #SELECT name,disc,place,time,length FROM events  WHERE time > NOW() ORDER BY time;
        info = db.check_events()
        count = db.count_events()
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.ui.ag_1.hide()
        self.ui.ag_2.hide()
        self.ui.ag_3.hide()
        if (count > 0):
            self.ui.ag_1.show()
            first_info = info[0]
            # 2021-05-20 15:49:58.127311+03:00
            self.ui.event_name.setText(first_info[0])
            self.ui.event_desc.setText(first_info[1])
            self.ui.event_place.setText(first_info[2])
            s_time = str(first_info[3])
            self.ui.event_date.setText(s_time[s_time.find(' ')+1:16])
            self.ui.event_time.setText(str(first_info[4]) + "min")
            self.ui.num_1.setText(s_time[8:10])
            print(f"\n{int(s_time[5:7])}\n")
            month = months[int(s_time[5:7]) - 1]
            self.ui.mon_1.setText(month)
        if (count > 1):
            self.ui.ag_2.show()
            second_info = info[1]
            self.ui.event_name_2.setText(second_info[0])
            self.ui.event_desc_2.setText(second_info[1])
            self.ui.event_place_2.setText(second_info[2])
            s_time = str(second_info[3])
            self.ui.event_date_2.setText(s_time[s_time.find(' ')+1:16])
            self.ui.event_time_2.setText(str(second_info[4]) + "min")
            self.ui.num_2.setText(s_time[8:10])
            # self.ui.mon_2.setText(second_info[6])
            month = months[int(s_time[5:7]) - 1]
            self.ui.mon_2.setText(month)
        if (count > 2):
            self.ui.ag_3.show()
            th_info = info[2]
            self.ui.event_name_3.setText(th_info[0])
            self.ui.event_desc_3.setText(th_info[1])
            self.ui.event_place_3.setText(th_info[2])
            s_time = str(th_info[3])
            self.ui.event_date_3.setText(s_time[s_time.find(' ') + 1:16])
            self.ui.event_long_3.setText(str(th_info[4]) + "min")
            self.ui.num_2.setText(s_time[8:10])
            # self.ui.mon_2.setText(second_info[6])
            month = months[int(s_time[5:7]) - 1]
            self.ui.man_3.setText(month)
    # sys.exit(app.exec_())


    def init_UI(self):
        self.setWindowTitle("diplome")
        av = f"/home/ramil/Desktop/pyqt/src_qt/avatar/{db.get_av()}.png"
        # print(av)
        self.ui.avatar.setPixmap(QtGui.QPixmap(av))
        self.ui.name.setText(db.get_name())
        # self.ui.avatar.setStyleSheet("border-radius: 5px;")


class Auth(QtWidgets.QMainWindow):
    def __init__(self):
        super(Auth, self).__init__()
        self.ui = Ui_Auth()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("diplome")
        self.setWindowIcon(QIcon("./img/fre-icon-avatar-126486.png"))
        self.ui.email.setPlaceholderText(" введите логин")
        self.ui.pwd.setPlaceholderText(" введите пароль")
        self.ui.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.login.clicked.connect(self.login)
        self.ui.logup.clicked.connect(self.logup)
        self.ui.no.hide()
    def logup(self):
        self.destroy()
        self.application = logup_win()
        self.application.show()
    def login(self):
        name = self.ui.email.text()
        real_pwd = None
        try:
            real_pwd = db.chaeck_pwd(name)
            # real_pwd = real_pwd[0]
            print(id)
        except TypeError:
            self.ui.no.show()
        pwd = self.ui.pwd.text()
        if (real_pwd and pwd == real_pwd):
            self.destroy()
            self.application = main_win()
            self.application.show()
            return (1)
        else:
            self.ui.no.show()
            return (0)
    # def logup(self):

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    application = Auth()
    db = db()
    application.show()
    sys.exit(app.exec_())
