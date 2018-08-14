# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Second(object):
    def setupUi(self, Second):
        Second.setObjectName("Second")
        Second.resize(400, 300)
        self.label = QtWidgets.QLabel(Second)
        self.label.setGeometry(QtCore.QRect(100, 120, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(Second)
        QtCore.QMetaObject.connectSlotsByName(Second)

    def retranslateUi(self, Second):
        _translate = QtCore.QCoreApplication.translate
        Second.setWindowTitle(_translate("Second", "Form"))
        self.label.setText(_translate("Second", "Label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second = QtWidgets.QWidget()
    ui = Ui_Second()
    ui.setupUi(Second)
    Second.show()
    sys.exit(app.exec_())

