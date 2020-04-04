import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout,QWidget
from PyQt5.QtGui import QIcon

class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow,self).__init__()

        self.setWindowTitle("我的第一个qt程序")
        self.resize(3000,1700)
        self.status = self.statusBar() #获取状态栏
        self.status.showMessage('只存在5秒的信息！',5000) #在状态栏中显示5秒的信息！
        self.button =QPushButton('开始')

        self.button.clicked.connect(self.buttonclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.mainframe = QWidget()
        self.mainframe.setLayout(self.layout)
        self.setCentralWidget(self.mainframe)

    def buttonclick(self):
        print('ok')
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/1.ico'))
    mainwind = FirstMainWindow()
    mainwind.show()
    sys.exit(app.exec_())
