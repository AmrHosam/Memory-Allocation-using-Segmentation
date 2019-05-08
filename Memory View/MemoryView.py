# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemoryView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets

from MemoryLayouts import *

import sys
sys.path.append("/home/omar/Projects/Memory-Allocation-using-Segmentation")
from window7 import *

import copy


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
        self.TitleLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.TitleLabel.setMinimumWidth(160)
        self.WindowContainerLayout.addWidget(self.TitleLabel)

        self.output_window = OutputWindow
        self.memory_data = memory_data

        self.MemoryInit()

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddBtn = QtWidgets.QPushButton(
            self.Memory.scrollAreaWidgetContents)
        self.AddBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.AddBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AddBtn.setObjectName("AddBtn")
        self.horizontalLayout.addWidget(self.AddBtn)
        self.CompactionBtn = QtWidgets.QPushButton(
            self.Memory.scrollAreaWidgetContents)
        self.CompactionBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.CompactionBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.CompactionBtn.setObjectName("CompactionBtn")
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.CompactionBtn)
        self.WindowContainerLayout.addLayout(self.horizontalLayout)
        self.OutputWindowLayout.addLayout(self.WindowContainerLayout)

        self.AddBtn.clicked.connect(self.AddProcess)
        self.CompactionBtn.clicked.connect(self.Compaction)

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

    def Compaction(self):
        self.Memory.MemData.compaction()
        self.memory_data = copy.deepcopy(self.Memory.MemData)
        self.Memory.RefreshContainer(self.memory_data, self)
        
    def AddProcess(self):
        self.segment_window= QtWidgets.QMainWindow()
        self.seg_ui = Ui_segment_window()
        self.seg_ui.setupUi(self.segment_window,self)
        self.segment_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    pro1 = Process()
    pro2 = Process()
    segments = [Segment("hole", 1000, 0, 0, True), Segment("Heap", 2000, pro1, 1000, False), Segment(
        "hole", 15, 0, 3000, True), Segment("Stack", 1500, pro1, 3015, False), Segment("Stack", 500, pro2, 4515, False)]
    data = Memory(segments)
    data.processes.append(pro1)
    data.processes.append(pro2)
    ui.setupUi(OutputWindow, data)
    OutputWindow.show()
    sys.exit(app.exec_())
