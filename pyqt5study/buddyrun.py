import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import buddy
from PyQt5 import QtCore
if __name__ == '__main__':
    def nameclick():
        # ui.lineEdit.setText('程超')
        content=ui.lineEdit.text()
        ui.lineEdit_2.setText(content)
        print('ok')
    def closeclick():
        app = QApplication.instance()
        app.quit()


    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #解决了Qtdesigner设计的界面与实际运行界面不一致的问题
    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = buddy.Ui_MainWindow()   
    ui.setupUi(mainwin)
    ui.pushButton.clicked.connect(nameclick)
    ui.pushButton_2.clicked.connect(closeclick)
    mainwin.show()
    sys.exit(app.exec_())