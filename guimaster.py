from firstgui import Ui_Dialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import standardsheet
import firstgui

class uiprogram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.confirm.clicked.connect(self.function)

    def function(self):
        print('clicked')
        firstgui.Ui_Dialog.openwindow(self)

    def func2(self):
        print('add')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = uiprogram(dialog)

    dialog.show()
    sys.exit(app.exec_())