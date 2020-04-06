from PyQt5.QtWidgets import *
import accountcheck
from PyQt5 import QtCore
import sys





if __name__ == '__main__':



    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #解决了Qtdesigner设计的界面与实际运行界面不一致的问题
    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = accountcheck.Ui_MainWindow()
    ui.setupUi(mainwin)
    ui.pushButton.clicked.connect(dataget)
    # ui.pushButton_2.clicked.connect(closeclick)
    mainwin.show()
    sys.exit(app.exec_())