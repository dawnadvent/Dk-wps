# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/PyCharm/untitled/wps/GUI/wps.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import imgs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 731, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.wps_sign_in_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wps_sign_in_Button.setObjectName("wps_sign_in_Button")
        self.gridLayout.addWidget(self.wps_sign_in_Button, 2, 2, 1, 1)
        self.sid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sid.setText("")
        self.sid.setObjectName("sid")
        self.gridLayout.addWidget(self.sid, 0, 1, 1, 1)
        self.userid = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userid.setText("")
        self.userid.setObjectName("userid")
        self.gridLayout.addWidget(self.userid, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.wps_invite_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.wps_invite_Button.setObjectName("wps_invite_Button")
        self.gridLayout.addWidget(self.wps_invite_Button, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dk-wps"))
        self.wps_sign_in_Button.setText(_translate("MainWindow", "邀请"))
        self.label.setText(_translate("MainWindow", "SID"))
        self.wps_invite_Button.setText(_translate("MainWindow", "签到"))
        self.label_2.setText(_translate("MainWindow", "USERID"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SID:</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">登录http://zt.wps.cn 获取cookie中wps_sid</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">USERID:</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">登录http://zt.wps.cn 个人中心获取用户id</p></body></html>"))
