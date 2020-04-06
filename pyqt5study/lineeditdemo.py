from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class LineEditdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        edit1 = QLineEdit()
        #设置校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))
        edit2.setAlignment(Qt.AlignRight)

        edit3 =QLineEdit()
        edit3.setInputMask('99_9999_99999;#')
        edit3.setAlignment(Qt.AlignRight)

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textchange)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.textpasswd)

        edit6 = QLineEdit()
        edit6.setReadOnly(True)

        formset =QFormLayout()
        formset.addRow('整数校验：',edit1)
        formset.addRow('浮点数校验',edit2)
        formset.addRow('inputmasl',edit3)
        formset.addRow('文本变化',edit4)
        formset.addRow('密码',edit5)
        formset.addRow('只读',edit6)
        self.setLayout(formset)
        self.setWindowTitle('lineedit综合案例')
    def textchange(self,text):
        print('输入内容'+text)

    def textpasswd(self):
        print('已经输入！')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwind = LineEditdemo()
    mainwind.show()
    sys.exit(app.exec_())