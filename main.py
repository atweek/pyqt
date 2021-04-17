from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys
from disigner.login import Ui_Dialog as Ui_Auth
#pyuic5.exe test.ui -o test.py -x

class Auth(QtWidgets.QMainWindow):
    def __init__(self):
        super(Auth , self).__init__()
        self.ui = Ui_Auth()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("diplome")
        self.setWindowIcon(QIcon("./img/free-icon-avatar-126486.png"))
        self.ui.login.text()
app = QtWidgets.QApplication([])
application = Auth()
application.show()

sys.exit(app.exec_())