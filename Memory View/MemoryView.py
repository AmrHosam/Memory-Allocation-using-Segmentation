# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemoryView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MemoryObjects import *


class Ui_OutputWindow(object):
    def setupUi(self, OutputWindow):
        OutputWindow.setObjectName("OutputWindow")
        OutputWindow.resize(294, 562)
        OutputWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.pushButton = QtWidgets.QPushButton(OutputWindow)
        self.pushButton.setGeometry(QtCore.QRect(100, 520, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.MemoryList = QtWidgets.QListWidget(OutputWindow)
        self.MemoryList.setGeometry(QtCore.QRect(65, 50, 211, 461))
        self.MemoryList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MemoryList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MemoryList.setObjectName("MemoryList")
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.MemoryList.addItem(item)
        self.label = QtWidgets.QLabel(OutputWindow)
        self.label.setGeometry(QtCore.QRect(120, 20, 67, 17))
        self.label.setObjectName("label")
        self.AddressList = QtWidgets.QListWidget(OutputWindow)
        self.AddressList.setGeometry(QtCore.QRect(15, 40, 50, 481))
        self.AddressList.setStyleSheet("background-color: rgb(242, 242, 242);\n"
                                       "")
        self.AddressList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AddressList.setObjectName("AddressList")

        self.retranslateUi(OutputWindow)
        QtCore.QMetaObject.connectSlotsByName(OutputWindow)

    def addSegment(self, segment):
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(115, 210, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        item.setSizeHint(QtCore.QSize(0, segment.length))
        pass

    def retranslateUi(self, OutputWindow):
        _translate = QtCore.QCoreApplication.translate
        OutputWindow.setWindowTitle(_translate("OutputWindow", "Memory View"))
        self.pushButton.setText(_translate("OutputWindow", "Add Process"))
        __sortingEnabled = self.MemoryList.isSortingEnabled()
        self.MemoryList.setSortingEnabled(False)
        item = self.MemoryList.item(0)
        item.setText(_translate("OutputWindow", "UT0"))
        self.MemoryList.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("OutputWindow", "Memory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    ui.setupUi(OutputWindow)
    OutputWindow.show()
    sys.exit(app.exec_())
