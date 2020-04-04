import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QHBoxLayout,QPushButton,QWidget,QVBoxLayout,QToolTip,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()

        self.setWindowTitle("我的第一个qt程序")
        self.resize(3000,1700)
        self.status = self.statusBar() #获取状态栏
        self.status.showMessage('只存在5秒的信息！',5000) #在状态栏中显示5秒的信息！

    def centerwindow(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newleft = (screen.width()-size.width())/2
        newtop = (screen.height()-size.height())/2
        self.move(newleft,newtop)

    def quitapplication(self):
        QToolTip.setFont(QFont('SansSerief',12))
        self.button1 = QPushButton('召唤程序关闭按钮')
        self.button1.clicked.connect(self.clickslot)
        self.button1.setToolTip("are you ok?")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.mainframe = QWidget()
        self.mainframe.setLayout(self.layout)
        self.setCentralWidget(self.mainframe)

    def clickslot(self):
        # sender = self.sender()
        print('召唤关闭按钮')
        self.button2 = QPushButton('我乃关闭按钮')
        self.button2.clicked.connect(self.clickslot2)
        self.button2.setToolTip('点击后程序关闭!')
        self.layout.addWidget(self.button2)
        self.mainframe.setLayout(self.layout)
        self.setCentralWidget(self.mainframe)

    def labelset(self):
        self.label1 = QLabel(self)
        self.label1.setText('<a href="http://www.baidu.com">label1</a>')
        self.label1.setToolTip('label')
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.linkActivated.connect(self.labelclick) #信号与槽部分有点问题了......
        self.label1.setOpenExternalLinks(True)
        self.label1.linkHovered.connect(self.labelclick) #label中需要有链接才能信号与槽连接成功!
        self.layout.addWidget(self.label1)
        self.mainframe.setLayout(self.layout)
        self.setCentralWidget(self.mainframe)

    def labelclick(self):
        print('label one has been clicked!')

    def clickslot2(self):
        app = QApplication.instance()  # 获取当前app的实例
        app.quit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/1.ico'))
    mainwind = QuitApplication()
    mainwind.show()
    mainwind.quitapplication()
    mainwind.centerwindow()
    mainwind.labelset()
    sys.exit(app.exec_())
