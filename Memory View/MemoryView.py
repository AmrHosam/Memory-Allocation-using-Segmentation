# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemoryView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets

from MemoryLayouts import *


class Ui_OutputWindow(object):
    def setupUi(self, OutputWindow, memory_data):
        OutputWindow.setObjectName("OutputWindow")
        OutputWindow.resize(437, 426)
        OutputWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.OutputWindowLayout = QtWidgets.QVBoxLayout(OutputWindow)
        self.OutputWindowLayout.setObjectName("OutputWindowLayout")
        self.WindowContainerLayout = QtWidgets.QVBoxLayout()
        self.WindowContainerLayout.setObjectName("WindowContainerLayout")

        self.TitleLabel = QtWidgets.QLabel(OutputWindow)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.WindowContainerLayout.addWidget(self.TitleLabel)

        self.output_window = OutputWindow
        self.memory_data = memory_data

        self.MemoryInit()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddBtn = QtWidgets.QPushButton(
            self.Memory.scrollAreaWidgetContents)
        self.AddBtn.setMaximumSize(QtCore.QSize(180, 16777215))
        self.AddBtn.setObjectName("AddBtn")
        self.horizontalLayout.addWidget(self.AddBtn)
        self.CompactionBtn = QtWidgets.QPushButton(
            self.Memory.scrollAreaWidgetContents)
        self.CompactionBtn.setMinimumSize(QtCore.QSize(180, 0))
        self.CompactionBtn.setMaximumSize(QtCore.QSize(180, 16777215))
        self.CompactionBtn.setObjectName("CompactionBtn")
        self.horizontalLayout.addWidget(self.CompactionBtn)
        self.WindowContainerLayout.addLayout(self.horizontalLayout)
        self.OutputWindowLayout.addLayout(self.WindowContainerLayout)

        self.AddBtn.clicked.connect(self.RefreshMemory)

        self.retranslateUi(OutputWindow)
        QtCore.QMetaObject.connectSlotsByName(OutputWindow)

    def retranslateUi(self, OutputWindow):
        _translate = QtCore.QCoreApplication.translate
        OutputWindow.setWindowTitle(_translate("OutputWindow", "Memory View"))
        self.AddBtn.setText(_translate("OutputWindow", "Add Process"))
        self.TitleLabel.setText(_translate("OutputWindow", "Memory"))
        self.CompactionBtn.setText(_translate("OutputWindow", "Compaction"))

    def RefreshMemory(self):
        self.memory_data = copy.deepcopy(self.Memory.MemData)
        self.Memory.RefreshContainer(self.memory_data, self)

    def MemoryInit(self):
        self.Memory = MemoryLayout(self.memory_data, self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    pro = Process()
    segments = [Segment("hole", 1000, 0, 0, True), Segment("Heap", 2000, pro, 1000, False), Segment(
        "hole", 15, 0, 3000, True), Segment("Stack", 1500, pro, 3015, False)]
    data = Memory(segments)
    data.processes.append(pro)
    ui.setupUi(OutputWindow, data)
    OutputWindow.show()
    sys.exit(app.exec_())
