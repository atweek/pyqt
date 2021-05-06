from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
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
    def init_UI(self):
        self.setWindowTitle("diplome")

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
            real_pwd = db.chaeck_pwd(name)[0]
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

app = QtWidgets.QApplication([])
application = Auth()
db = db()
application.show()
sys.exit(app.exec_())
