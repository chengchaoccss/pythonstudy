# # 第一例：Pyqt5安装后测试，生成窗口
# import sys
# from PyQt5 import QtWidgets,QtCore
# app = QtWidgets.QApplication(sys.argv)
# widget = QtWidgets.QWidget()
# widget.resize(360,360)
# widget.setWindowTitle('hello pyqt5')
# widget.show()
# sys.exit(app.exec_())


# #第二例：Qwidget类的使用手册保存到本地硬盘上,可以使用这种方式把打印的内容存入本地文件
# import sys
# from PyQt5.QtWidgets import QWidget
# # out = sys.stdout
# sys.stdout = open('Qwidget.txt','w')
# help(QWidget)
# print('这些文字会被存到本地文件中！')
# sys.stdout.close()
# # sys.stdout = out

#第三例：面向对象方法实现窗口建立
#
# import sys
# from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
# class WinForm(QWidget):
#     def __init__(self,parent =None):
#         super(WinForm,self).__init__(parent)
#         self.setGeometry(300,300,350,350)
#         self.setWindowTitle('点击按钮关闭窗口！')
#         quit=QPushButton('close',self)
#         quit.setStyleSheet("background-color:red")
#         quit.clicked.connect(self.close)
#
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     win = WinForm()
#     win.show()
#     sys.exit((app.exec_()))

# 第四例：导入ui转成的py文件
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from secondsignal import Ui_MainWindow
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())