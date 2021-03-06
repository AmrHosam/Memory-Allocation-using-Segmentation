# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFrame
from PyQt5.QtWidgets import QLineEdit
import math
from MemoryObjects import Process, Segment
from MemoryView import *


class Ui_input_window(object):
    def setupUi(self, input_window):
        input_window.setObjectName("input_window")
        input_window.resize(414, 408)
        self.windowLayout = QtWidgets.QVBoxLayout(input_window)
        self.windowLayout.setObjectName("windowLayout")
        self.container = QtWidgets.QVBoxLayout()
        self.container.setObjectName("container")
        self.widget1 = QtWidgets.QWidget()
        #self.widget1.setGeometry(QtCore.QRect(70, 10, 221, 61))
        self.widget1.setObjectName("widget1")
        self.widget1.maximumHeight()
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        # self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.size = QtWidgets.QLineEdit(self.widget1)
        self.size.setObjectName("size")
        self.verticalLayout.addWidget(self.size)
        self.holes = QtWidgets.QSpinBox(self.widget1)
        self.holes.setMaximum(1000000)
        self.holes.setObjectName("holes")
        self.verticalLayout.addWidget(self.holes)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(input_window)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        # self.error.setGeometry(QtCore.QRect(0, 10, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.error.setFont(font)
        self.error.setObjectName("label")
        self.error.setStyleSheet("color: red")
        self.error.setText("ay klam")
        self.error.hide()
        self.windowLayout.addWidget(self.error)
        self.container.addWidget(self.widget1)
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(input_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 140, 241, 234))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(113)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.btnLayout)
        self.container.addWidget(self.layoutWidget1)
        # self.pushButton.hide()
        # self.tableWidget.hide()
        self.windowLayout.addLayout(self.container)
        self.holes.valueChanged.connect(self.set_rows)
        self.pushButton.clicked.connect(self.read_input)
        self.retranslateUi(input_window)
        QtCore.QMetaObject.connectSlotsByName(input_window)
        input_window.setTabOrder(self.size, self.holes)
        input_window.setTabOrder(self.holes, self.tableWidget)
        input_window.setTabOrder(self.tableWidget, self.pushButton)

    def retranslateUi(self, input_window):
        _translate = QtCore.QCoreApplication.translate
        input_window.setWindowTitle(_translate("input_window", "Input"))
        self.label.setText(_translate("input_window", "Memory size"))
        self.label_2.setText(_translate("input_window", "Number of holes"))
        self.pushButton.setText(_translate("input_window", "Allocate"))
        self.tableWidget.horizontalHeaderItem(0).setText("Base")
        item = self.tableWidget.horizontalHeaderItem(1).setText("Size")

    def set_rows(self):
        self.tableWidget.setRowCount(self.holes.value())
        self.tableWidget.show()
        self.pushButton.show()

    def mem_init(self, mem_holes):
        mem_segments = []
        seg_base = 0
        old = Process()
        Process.count = 0
        old.name = "Old Process"
        i = 0
        for row in range(0, len(mem_holes)):
            length = mem_holes[row][0] - seg_base
            if(length > 0):
                mem_segments.append(
                    Segment("Old Segment" + str(i), length, old, seg_base, False))
                seg_base = seg_base + length
            mem_segments.append(
                Segment("hole", mem_holes[row][1], 0, mem_holes[row][0], True))
            seg_base = seg_base + mem_holes[row][1]
            i += 1
        length = int(self.size.text()) - seg_base
        if(length > 0):
            mem_segments.append(
                Segment("Old Segment" + str(i), length, old, seg_base, False))
        return mem_segments

    def read_input(self):
        error = ""
        memory_size = str(self.size.text())
        if(not memory_size.isdigit()):
            error = "Memory size must be a postive integer"
        else:
            memory_size = int(memory_size)
            if(memory_size <= 0):
                error = "Memory size must be greater than 0"
        if(error == ""):
            holes = []
            no_holes = int(self.holes.text())
            for row in range(0, no_holes):
                hole_size = str(self.tableWidget.item(row, 1).text())
                hole_base = str(self.tableWidget.item(row, 0).text())
                if(not hole_base.isdigit()):
                    error = "Hole base must be a postive integer"
                    break
                else:
                    hole_base = int(hole_base)
                    if(hole_base < 0):
                        error = "Hole base must be a postive integer"
                        break
                    if(row > 0):
                        if(hole_base <= (holes[row-1][0] + holes[row-1][1])):
                            error = "Holes must be separated"
                            break
                if(not hole_size.isdigit()):
                    error = "Hole size must be a postive integer"
                    break
                else:
                    hole_size = int(hole_size)
                    if(hole_size <= 0):
                        error = "Hole size must be greater than 0"
                        break
                    if(hole_size + hole_base > memory_size):
                        error = "Out of bounds"
                        break
                holes.append([hole_base, hole_size])
            if(error == ""):
                self.error.hide()
                segs = self.mem_init(holes)
                mem = Memory(segs)
                # for i in range(len(segs)):
                #     print(str(segs[i].base)+"    " +segs[i].name+"   "+str(segs[i].length))
                self.memory_window = QtWidgets.QWidget()
                self.mem_ui = Ui_OutputWindow()
                self.mem_ui.setupUi(self.memory_window, mem)
                self.memory_window.show()
                return
        self.error.setText(error)
        self.error.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    input_window = QtWidgets.QWidget()
    ui = Ui_input_window()
    ui.setupUi(input_window)
    input_window.show()
    sys.exit(app.exec_())
