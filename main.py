from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys
import psycopg2
from disigner.login import Ui_Dialog as Ui_Auth
from disigner.mainwin import Ui_Dialog as Ui_MAIN


# conn = psycopg.connect("dbname=test user=postgres")
#pyuic5.exe test.ui -o test.py -x

class db():
    def __init__(self):
        self.conn = psycopg2.connect(user="ramil",
                                password="ramille",
                                host="127.0.0.1",
                                port="5432")
        cur = self.conn.cursor()
        cur.execute("SELECT version();\n")
        print(cur.fetchall())
        cur.close()
    def get_login(self,name):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT pwd FROM users WHERE name = '{name}';")
        pwd = cursor.fetchone()
        cursor.close()
        return pwd

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
        self.ui.login.clicked.connect(self.login)
        # self.ui.logup.clicked.connect(self.logup())
        self.ui.no.hide()
    def login(self):
        name = self.ui.email.text()
        real_pwd = None
        try:
            real_pwd = db.get_login(name)[0]
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