from PyQt5.QtCore import QObject,pyqtSignal

#创建信号对象
class QTypeSignal(QObject):
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super().__init__()
    def run(self):
        self.sendmsg.emit('hello pyqt5')

#创建槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super().__init__()
    def get(self,msg):
        print('data is :'+msg)

if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()
    # 绑定信号与槽
    print('bangding')
    send.sendmsg.connect(slot.get)
    send.run()
    #解绑
    print('jiebang')
    send.sendmsg.disconnect(slot.get)
    send.run()