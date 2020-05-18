import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_wps import *
from wps import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.wps_invite_Button.clicked.connect(self.display_wps_invite)
        # 添加退出按钮信号和槽。调用close函数
        self.wps_sign_in_Button.clicked.connect(self.display_wps_sign_in)

    def display_wps_invite(self):
        # 利用line Edit控件对象text()函数获取界面输入
        sid = self.sid.text()
        msgtextlog = wps_invite(sid)
        self.textBrowser.setText(msgtextlog)
        # 利用text Browser控件对象setText()函数设置界面显示

    def display_wps_sign_in(self):
        userid = self.userid.text()
        msgtextlog = wps_sign_in(userid)
        for i in msgtextlog:
            self.textBrowser.append(i)
            QtWidgets.QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
