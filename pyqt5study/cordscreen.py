import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QHBoxLayout,QPushButton,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon

def clickedevent():
    print(f'{widget.x()}')
    app = QApplication.instance()
    app.quit()


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(clickedevent)
widget.resize(400,400)
widget.move(250,250)
widget.show()
sys.exit(app.exec_())
