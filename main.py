from PyQt5 import QtWidgets, QtGui ,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
ftom Q
import sys

#pyuic5.exe test.ui -o test.py -x

# from PyQt5.Qt import *

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("test")
    window.setGeometry(300, 250, 350, 200)
    # window.height(680)
    # window.minimumHeight(680)
    # window.minimumWidth(920)
    # window.Width(920)
    # window.resize(920, 680)
    main_text = QtWidgets.QLabel("dwdwd")


    window.show()
    # sys.exit(app.exit())
    sys.exit(app.exec_())

if __name__ == "__main__":
        application()
