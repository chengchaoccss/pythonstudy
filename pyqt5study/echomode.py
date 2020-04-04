from PyQt5.QtWidgets import *
import sys

class Echomode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        formlayout =QFormLayout()
        normalmode = QLineEdit()
        noecho = QLineEdit()
        passed = QLineEdit()
        passedecho = QLineEdit()

        #注意formlayout添加控件的方式：addrow。
        formlayout.addRow('normalmode',normalmode)
        formlayout.addRow('noecho',noecho)
        formlayout.addRow('passwd',passed)
        formlayout.addRow('passedecho',passedecho)

        #plassholdertext,也就是设置文本输入框内提示信息。
        normalmode.setPlaceholderText('normalmode')
        noecho.setPlaceholderText('noecho')
        passed.setPlaceholderText('passed')
        passedecho.setPlaceholderText('passedecho')
        self.setLayout(formlayout)

        #四种模式设置，感觉一般是第三种中较多，也就是不显示密码具体内容
        normalmode.setEchoMode(QLineEdit.Normal)
        noecho.setEchoMode(QLineEdit.NoEcho)
        passed.setEchoMode(QLineEdit.Password)
        passedecho.setEchoMode(QLineEdit.PasswordEchoOnEdit)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainwind = Echomode()
    mainwind.show()
    sys.exit(app.exec_())