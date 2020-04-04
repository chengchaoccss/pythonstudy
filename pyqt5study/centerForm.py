import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/1.ico'))
    mainwind = CenterForm()
    mainwind.show()
    mainwind.centerwindow()
    sys.exit(app.exec_())
