# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from selenium import webdriver
import time, json, os
from hello import *


class Ui_Form(QtWidgets.QMainWindow):

    def __init__(self):
        self.login_cookies = {}
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(210, 154)

        # user
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 71, 20))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")

        # user_input
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # password
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 70, 71, 20))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")

        # password_input
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 70, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        # remeber_all
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(130, 100, 71, 16))
        self.checkBox.setObjectName("checkBox")
        # self.checkBox.stateChanged.connect(self.checked)

        #login push button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)

        # setting input value
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        number = QRegExp("[0-9]*")
        validator_num = QRegExpValidator(number, self.lineEdit_2)
        self.lineEdit_2.setValidator(validator_num)

        #  初始化登录信息
        self.info_login()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "login"))
        self.lineEdit.setText(_translate("Form", "用户名："))
        self.lineEdit_3.setText(_translate("Form", "密  码："))
        self.checkBox.setText(_translate("Form", "保存密码"))
        self.pushButton.setText(_translate("Form", "登录"))

    def clicked(self):

        if self.checkBox.isChecked():
            a = {
                'user':self.lineEdit_2.text(),
                'pasw':self.lineEdit_4.text()
            }
            with open('ww.json','w') as w:
                w.write(json.dumps(a))

        if self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '账号为空')
            return
        if self.lineEdit_4.text() == "":
            QMessageBox.warning(self, '警告', '密码为空')
            return
        else:
            QMessageBox.warning(self, "警告", "程序将自动运行，为方便您的操作请勿操作")

            browser = webdriver.PhantomJS()
            # 等待3秒，用于等待浏览器启动完成，否则可能报错
            time.sleep(5)
            browser.get(
                "url")  # ①

            def logined():

                # 找到 账号和密码表单 并 清空
                id = browser.find_element_by_id('username')
                password = browser.find_element_by_id('password')
                id.clear()
                password.clear()

                # 输入值 并提交
                id.send_keys(self.lineEdit_2.text())
                password.send_keys(self.lineEdit_4.text())
                browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button').click()

                # 判断是否登录成功
                if browser.title == '统一身份认证':
                    browser.close()
                    QMessageBox.warning(self, '警告', '用户名或密码错误')
                    self.lineEdit_4.setText('')
                    # 密码错误
                    return
                else:
                    # 《《《《《《《《《《《《登录成功》》》》》》》》》》》
                    cookies = browser.get_cookies()
                    Ui_Check.show()
                    Form.close()
                time.sleep(2)
                for cookie in cookies:
                    self.login_cookies[cookie['name']] = cookie['value']
                browser.close()
                self.write_cookie()

            return logined()


    def write_cookie(self):
        with open('cookies.json','w') as tim:
            tim.write(json.dumps(self.login_cookies))

    # 初始化登录信息
    def info_login(self):
        if os.path.exists('ww.json') == True:
            with open('ww.json','r')as fw:
                str = fw.read()
                data = json.loads(str)
            self.lineEdit_2.setText(data['user'])
            self.lineEdit_4.setText(data['pasw'])
            self.checkBox.setChecked(True)
        else:
            pass


    # def check_cookietime(self):
    #     if os.path.exists('cookies.json') == True:
    #         xiugai = os.stat("cookies.json").st_mtime
    #         tii = time.localtime(xiugai)
    #         dt_niew = time.strftime("%Y%m%d%H%M%S", tii)
    #         dt_now = time.time()
    #         local_now = time.localtime(dt_now)
    #         dt_now = time.strftime("%Y%m%d%H%M%S", local_now)
    #         print(dt_niew)
    #         print(dt_now)
    #         day = int(dt_now) - int(dt_niew)
    #         if day > 10000:
    #             QMessageBox.warning(self,'警告','请重新登录')
    #             return Form.show()
    #         else:
    #             with open('cookies.json','r') as r:
    #                 str = r.read()
    #                 date = json.loads(str)
    #                 self.login_cookies = date
    #                 azz = QtWidgets.QWidget()
    #                 ui = hello_mainWindow()
    #                 ui.setupUi(azz)
    #                 ui.show()
    #     else:
    #         return Form.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    Ui_Check = hello_mainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

