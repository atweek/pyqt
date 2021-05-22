# from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt
from disigner.login import Ui_Dialog as Ui_Auth
from disigner.mainwin import Ui_Dialog as Ui_MAIN
from disigner.singup import Ui_Dialog as Ui_LOGUP
from disigner.tasks import Ui_Dialog as UI_TASKS
from db import db
import datetime
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
            db.logup(self.ui.name.text(), self.ui.pwd.text(), self.ui.phone.text(),
                     self.ui.email.text(), self.ui.tg.text())
            self.destroy()
            application = Auth()
            application.show()
    def init_UI(self):
        self.setWindowTitle("diplome")
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            exit(0)

class tasks_win(QtWidgets.QMainWindow):
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
            exit(0)
    def __init__(self):
        super(tasks_win, self).__init__()
        self.ui = UI_TASKS()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):

        def init_add_task():
            name = self.ui.name.text()
            text = self.ui.textEdit.toPlainText()
            date = str(self.ui.dateEdit.date())
            if (db.add_task(name,text,date) == 0):
                self.ui.label_3.show()
            else:
                self.destroy()
            # main_win.update(main_win.init_UI())

        self.ui.label_3.hide()
        self.setWindowTitle("diplome")
        self.ui.dateEdit.setDate(datetime.date.today())
        self.ui.name.setPlaceholderText("  enter the recipient's nickname")
        self.ui.textEdit.setPlaceholderText("  enter task")
        self.ui.push.clicked.connect(init_add_task)
        # main_win.destroy(


class main_win(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_win, self).__init__()
        self.ui = Ui_MAIN()
        self.ui.setupUi(self)
        self.init_UI()
        self.init_events()
        self.off_task()
        self.on_task()
        self.init_task()
        self.ui.checkBox.clicked.connect(self.del_tasc_1)
        self.ui.checkBox_2.clicked.connect(self.del_tasc_2)
        self.ui.checkBox_3.clicked.connect(self.del_tasc_3)
        self.ui.checkBox_4.clicked.connect(self.del_tasc_4)
        self.ui.checkBox_5.clicked.connect(self.del_tasc_5)
        self.ui.checkBox_6.clicked.connect(self.del_tasc_6)
        self.ui.checkBox_7.clicked.connect(self.del_tasc_7)
        self.ui.checkBox_8.clicked.connect(self.del_tasc_8)
        self.ui.checkBox_9.clicked.connect(self.del_tasc_9)
        self.ui.checkBox_10.clicked.connect(self.del_tasc_10)
        self.ui.toolButton.clicked.connect(self.add_task)
        self.ui.main.clicked.connect(self.rest)
        self.ui.tasks.clicked.connect(self.add_task)

    def rest(self):
        self.destroy()
        self.application = main_win()
        self.application.show()
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
            exit(0)

    # def update(self):
    #
    #     self.on_task()
    #     self.init_task()

    def add_task(self):
        self.application_2 = tasks_win()
        self.application_2.show()
    def del_tasc_1(self):
        self.ui.task_1.hide()
        db.del_task(self.info[0][2])
    def del_tasc_2(self):
        self.ui.task_2.hide()
        db.del_task(self.info[1][2])
    def del_tasc_3(self):
        self.ui.task_3.hide()
        db.del_task(self.info[2][2])
    def del_tasc_4(self):
        self.ui.task_4.hide()
        db.del_task(self.info[3][2])
    def del_tasc_5(self):
        self.ui.task_5.hide()
        db.del_task(self.info[4][2])
    def del_tasc_6(self):
        self.ui.task_6.hide()
        db.del_task(self.info[5][2])
    def del_tasc_7(self):
        self.ui.task_7.hide()
        db.del_task(self.info[6][2])
    def del_tasc_8(self):
        self.ui.task_8.hide()
        db.del_task(self.info[7][2])
    def del_tasc_9(self):
        self.ui.task_9.hide()
        db.del_task(self.info[8][2])
    def del_tasc_10(self):
        self.ui.task_10.hide()
        db.del_task(self.info[9][2])

    def init_task(self):
        self.info = db.check_tasks()
        if (self.count_t > 0):
            self.ui.tdesc_1.setText(self.info[0][0])
            self.ui.name_1.setText("from: " + self.info[0][1])
            self.ui.t_date_1.setText("up to: " + str(self.info[0][3]))
            print(str(self.info[0][3]))
        if (self.count_t > 1):
            self.ui.tdesc_2.setText(self.info[1][0])
            self.ui.name_2.setText("from: " + self.info[1][1])
            self.ui.t_date_2.setText("up to: " + str(self.info[1][3]))
        if (self.count_t > 2):
            self.ui.tdesc_3.setText(self.info[2][0])
            self.ui.name_3.setText("from: " + self.info[2][1])
            self.ui.t_date_3.setText("up to: " + str(self.info[2][3]))
        if (self.count_t > 3):
            self.ui.tdesc_4.setText(self.info[3][0])
            self.ui.name_4.setText("from: " + self.info[3][1])
            self.ui.t_date_4.setText("up to: " + str(self.info[3][3]))
        if (self.count_t > 4):
            self.ui.tdesc_5.setText(self.info[4][0])
            self.ui.name_5.setText("from: " + self.info[4][1])
            self.ui.t_date_5.setText("up to: " + str(self.info[4][3]))
        if (self.count_t > 5):
            self.ui.tdesc_6.setText(self.info[5][0])
            self.ui.name_6.setText("from: " + self.info[5][1])
            self.ui.t_date_6.setText("up to: " + str(self.info[5][3]))
        if (self.count_t > 6):
            self.ui.tdesc_7.setText(self.info[6][0])
            self.ui.name_7.setText("from: " + self.info[6][1])
            self.ui.t_date_7.setText("up to: " + str(self.info[6][3]))
        if (self.count_t > 7):
            self.ui.tdesc_8.setText(self.info[7][0])
            self.ui.name_8.setText("from: " + self.info[7][1])
            self.ui.t_date_8.setText("up to: " + str(self.info[7][3]))
        if (self.count_t > 8):
            self.ui.tdesc_9.setText(self.info[8][0])
            self.ui.name_9.setText("from: " + self.info[8][1])
            self.ui.t_date_9.setText("up to: " + str(self.info[8][3]))
        if (self.count_t > 9):
            self.ui.tdesc_10.setText(self.info[9][0])
            self.ui.name_10.setText("from: " + self.info[9][1])
            self.ui.t_date_10.setText("up to: " + str(self.info[9][3]))

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
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
            exit(0)
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
