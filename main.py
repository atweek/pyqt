from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys
import psycopg2
from disigner.login import Ui_Dialog as Ui_Auth
from disigner.mainwin import Ui_Dialog as Ui_MAIN

#pyuic5.exe test.ui -o test.py -x

# class db():
#     def __init__(self):
#         # try:
        #     # self.con = psycopg2.connect(dbname='diploma', user='postgres', password='123',host='127.0.0.1')
        #     cursor = self.con.cursor()
        #     print(self.con.get_dsn_parameters(), "\n")
        #     cursor.execute("SELECT version();")
        #     record = cursor.fetchone()
        #     print("You are connected to - ", record, "\n")
        #     cursor.close()
        # except (Exception, psycopg2.Error) as error:
    #     #     print("Error while connecting to PostgreSQL", error)
    # def get_login(self):
    #     cursor = self.con.cursor()
    #     cursor.execute("SELECT login FROM users;")
    #     self.name = cursor.fetchone()

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
        super(Auth , self).__init__()
        self.ui = Ui_Auth()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("diplome")
        self.setWindowIcon(QIcon("./img/fre-icon-avatar-126486.png"))
        self.ui.email.setPlaceholderText(" введите логин")
        self.ui.pwd.setPlaceholderText(" введите пароль")
        self.ui.login.clicked.connect(self.get_info)
        self.ui.no.hide()
    def get_info(self):
        email = self.ui.email.text()
        pwd = self.ui.pwd.text()
        if (email == "123" and pwd == "123"):
            print("y")
            return (1)
            application.hide()
        else:
            self.ui.no.show()
            # self.ui.login.windowIconTextChanged()
            return (0)

app = QtWidgets.QApplication([])
application = Auth()
application.show()

sys.exit(app.exec_())