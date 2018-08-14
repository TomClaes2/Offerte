# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstgui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from secondgui import Ui_Second
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def openwindow(self):
        print('openwindow')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Second
        self.ui.setupUi(self, self.window)
        self.window.show()

    def test(self):
        print('test')

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.plainTextEdititems = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdititems.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.plainTextEdititems.setObjectName("plainTextEdititems")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 16))
        self.label.setObjectName("label")
        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setGeometry(QtCore.QRect(50, 100, 75, 23))
        self.confirm.setObjectName("confirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hoeveel items worden toegevoegd?"))
        self.confirm.setText(_translate("Dialog", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

