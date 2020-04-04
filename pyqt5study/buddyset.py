from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore

class Buddyset(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('label与伙伴关系')
        namelabel = QLabel('&Name',self)
        nameedit = QLineEdit(self)
        namelabel.setBuddy(nameedit)
        passwdlabel = QLabel('&Password',self)
        passedit = QLineEdit(self)
        passwdlabel.setBuddy(passedit)
        btnOk = QPushButton('&Ok')
        btnCancel = QPushButton('&Cancel')
        mainlayout =QGridLayout(self)
        mainlayout.addWidget(namelabel,0,0)
        mainlayout.addWidget(nameedit,0,1,1,2)
        mainlayout.addWidget(passwdlabel,1,0)
        mainlayout.addWidget(passedit,1,1,1,2)
        mainlayout.addWidget(btnOk,2,1)
        mainlayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainwind= Buddyset()
    mainwind.show()
    sys.exit(app.exec_())


