# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MemoryObjects import *


class Ui_segment_window(object):
    def setupUi(self, segment_window, output_window):
        self.memdata = output_window.Memory.MemData
        segment_window.setObjectName("segment_window")
        segment_window.resize(400, 300)
        self.windowVLayout = QtWidgets.QVBoxLayout(segment_window)
        self.window = segment_window
        self.output_window = output_window

        self.error = QtWidgets.QLabel(segment_window)
        self.error.setFixedSize(400, 100)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.error.setFont(font)
        self.error.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error.setLineWidth(1)
        self.error.setTextFormat(QtCore.Qt.PlainText)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.error.setStyleSheet("color: red")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.windowVLayout.addWidget(self.error)

        # self.verticalLayoutWidgt = QtWidgets.QWidget(segment_window)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.allocation_type = QtWidgets.QComboBox()
        self.allocation_type.setObjectName("allocation_type")
        self.allocation_type.addItem("")
        self.allocation_type.addItem("")
        self.allocation_type.addItem("")
        self.horizontalLayout.addWidget(self.allocation_type)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.no_segment = QtWidgets.QSpinBox()
        self.no_segment.setEnabled(True)
        self.no_segment.setReadOnly(False)
        self.no_segment.setAccelerated(False)
        self.no_segment.setKeyboardTracking(True)
        self.no_segment.setMinimum(1)
        self.no_segment.setObjectName("no_segment")
        self.horizontalLayout_2.addWidget(self.no_segment)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.windowVLayout.addLayout(self.verticalLayout)

        self.segment_table = QtWidgets.QTableWidget()
        self.segment_table.setEnabled(True)
        self.segment_table.setMinimumHeight(200)
        self.segment_table.setMinimumWidth(250)
        self.segment_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.segment_table.setRowCount(1)
        self.segment_table.setColumnCount(2)
        self.segment_table.setObjectName("segment_table")
        item = QtWidgets.QTableWidgetItem()
        self.segment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.segment_table.setHorizontalHeaderItem(1, item)
        self.tableLayout = QtWidgets.QHBoxLayout()
        self.tableLayout.addWidget(self.segment_table)
        self.windowVLayout.addLayout(self.tableLayout)

        self.enter = QtWidgets.QPushButton()
        self.enter.setObjectName("enter")
        self.enter.setMaximumWidth(200)
        self.btnLayout = QtWidgets.QHBoxLayout()
        self.btnLayout.addWidget(self.enter)
        self.windowVLayout.addLayout(self.btnLayout)

        # self.menubar = QtWidgets.QMenuBar(segment_window)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        # self.menubar.setObjectName("menubar")
        # segment_window.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(segment_window)
        # self.statusbar.setObjectName("statusbar")
        # segment_window.setStatusBar(self.statusbar)
        self.retranslateUi(segment_window)
        QtCore.QMetaObject.connectSlotsByName(segment_window)

        self.no_segment.setMaximum(1000000000)

    def retranslateUi(self, segment_window):
        _translate = QtCore.QCoreApplication.translate
        segment_window.setWindowTitle(
            _translate("segment_window", "Enter Process"))
        self.label_2.setText(_translate(
            "segment_window", "method of allocation "))
        self.allocation_type.setItemText(
            0, _translate("segment_window", "First fit "))
        self.allocation_type.setItemText(
            1, _translate("segment_window", "Best fit"))
        self.allocation_type.setItemText(
            2, _translate("segment_window", "Worst fit"))
        self.label.setText(_translate("segment_window", "no of segments"))
        item = self.segment_table.horizontalHeaderItem(0)
        item.setText(_translate("segment_window", "Name"))
        item = self.segment_table.horizontalHeaderItem(1)
        item.setText(_translate("segment_window", "Size"))
        self.enter.setText(_translate("segment_window", "Enter"))
        self.error.setText(_translate("segment_window", "omar"))

        self.no_segment.valueChanged.connect(self.show_hide)
        # self.segment_table.hide()
        self.error.hide()
        # self.enter.hide()
        self.enter.clicked.connect(self.ReadTable)

    def get_allocation(self):
        index = self.allocation_type.currentIndex()
        return index

    def get_no_segements(self):
        num = self.no_segment.value()
        return num

    def show_hide(self):
        i = self.get_no_segements()
        self.segment_table.hide()
        self.segment_table.setRowCount(i)
        self.segment_table.show()
        self.enter.show()

        # self.error.setText(_translate("segment_window", error))
    def ReadTable(self):
        alloc = self.get_allocation()
        seg_list = []
        error = ""
        out = Process()
        success = bool

        self.memdata = self.output_window.Memory.MemData

        num = self.get_no_segements()
        print(self.segment_table.item(0, 0))
        for row in range(num):
            it = self.segment_table.item(row, 0)
            if it == None:
                name = ""
            else:
                name = str(self.segment_table.item(row, 0).text())
            if(name == ""):
                error = name + "Segement name is required"
                break

            it = self.segment_table.item(row, 1)
            if it == None:
                size = ""
            else:
                size = self.segment_table.item(row, 1).text()

            if(not size.isdigit()):
                error = name + " size must be a postive integer"
                break
            elif(size == ""):
                error = name + "Segement size is required"
                break
            else:
                size = int(size)
            if(size < 0):
                error = name + " size must be >= 0"
                break
        if(error != ""):
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate("segment_window", error))
            self.error.show()
            return
        for row in range(num):
            s = Segment(str(self.segment_table.item(row, 0).text()),
                        int(self.segment_table.item(row, 1).text()), out)
            seg_list.append(s)
        if (alloc == 0):  # first fit
            success = self.memdata.firstFit(out)
        elif (alloc == 1):  # Best fit
            success = self.memdata.bestFit(out)
        elif (alloc == 2):  # worst fit
            success = self.memdata.worstFit(out)
        if(success == False):
            error = "Must deallocate"
            _translate = QtCore.QCoreApplication.translate
            self.error.setText(_translate("segment_window", error))
            self.error.show()
        else:
            self.output_window.RefreshMemory()
            self.window.close()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     segment_window= QtWidgets.QMainWindow()
#     ui = Ui_segment_window()
#     pro1 = Process()
#     pro2 = Process()
#     segments = [Segment("hole", 1000, 0, 0, True), Segment("Heap", 2000, pro1, 1000, False), Segment(
#         "hole", 15, 0, 3000, True), Segment("Stack", 1500, pro1, 3015, False), Segment("Stack", 500, pro2, 4515, False)]
#     data = Memory(segments)
#     data.processes.append(pro1)
#     data.processes.append(pro2)
#     ui.setupUi(segment_window, data)
#     segment_window.show()
    # sys.exit(app.exec_())
