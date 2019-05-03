# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemoryView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MemoryObjects import *
import random


class MemoryLayout:
    Height = 450
    Width = 181
    X = 60
    Y = 40

    def __init__(self, data, window):
        self.segments = []
        self.MemData = []
        self.MemData = copy.deepcopy(data)
        lastSegment = self.MemData.segments[len(self.MemData.segments)-1]
        self.totalLocationsNum = lastSegment.base + lastSegment.length + 1
        self.ratio = 900 / self.totalLocationsNum

        self.scrollArea = QtWidgets.QScrollArea(window)
        self.scrollArea.setGeometry(QtCore.QRect(
            MemoryLayout.X, MemoryLayout.Y, MemoryLayout.Width, MemoryLayout.Height))
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("MemoryLayout")

        self.WidgetContainer = QtWidgets.QWidget()
        self.containerHeight = 900

        self.RefreshContainer(copy.deepcopy(self.MemData))

    def RefreshContainer(self, data):
        self.MemData.segments.clear()
        self.MemData.processes.clear()
        self.segments.clear()
        del self.WidgetContainer
        del self.MemData
        del self.segments
        self.segments = []
        self.MemData = []
        self.MemData = copy.deepcopy(data)
        self.WidgetContainer = QtWidgets.QWidget()
        self.WidgetContainer.setGeometry(QtCore.QRect(0, 0, 165, 900))
        self.WidgetContainer.setObjectName("WidgetContainer")
        self.__AddContents()
        self.scrollArea.setWidget(self.WidgetContainer)

    def __AddContents(self):
        for segment in self.MemData.segments:
            self.segments.append(SegmentLayout(self, segment))


class SegmentLayout:
    segmentWidth = 165
    nameLabelWidth = 100
    nameLabel_x = 65
    limitLabelWidth = 60
    minSegmentHeight = 30
    segmentCount = 0
    nextY = 0
    holeColor = "rgb(155, 155, 155)"

    def __init__(self, memory_layout, segment):  # edit here
        color = []
        color.append(random.randrange(0, 256))
        color.append(random.randrange(0, 256))
        color.append(random.randrange(0, 256))
        i = random.randrange(0, 3)
        color[i] = 0
        self.color = "rgb("+str(color[0]) + ", " + \
            str(color[1]) + ", "+str(color[2]) + ")"
        if segment.free:
            self.color = SegmentLayout.holeColor
            parentName = ""
        else:
            parentName = "\n("+segment.parentProcess.name+")"

        self.SegmentData = segment

        h = memory_layout.ratio * self.SegmentData.length
        if h < SegmentLayout.minSegmentHeight:
            memory_layout.WidgetContainer.setFixedHeight(
                memory_layout.containerHeight + SegmentLayout.minSegmentHeight - h)
            memory_layout.containerHeight += SegmentLayout.minSegmentHeight - h
            h = SegmentLayout.minSegmentHeight
        y = SegmentLayout.nextY

        self.segmentWidget = QtWidgets.QWidget(memory_layout.WidgetContainer)
        self.segmentWidget.setGeometry(
            QtCore.QRect(0, y, SegmentLayout.segmentWidth, h))
        self.segmentWidget.setObjectName(
            "segment_"+str(SegmentLayout.segmentCount))
        self.segmentWidget.setStyleSheet(
            "background-color: "+self.color+";")

        self.nameLabel = QtWidgets.QLabel(self.segmentWidget)
        self.nameLabel.setGeometry(QtCore.QRect(
            SegmentLayout.nameLabel_x, 0, SegmentLayout.nameLabelWidth, h))
        self.nameLabel.setObjectName(
            "nameLabel_"+str(SegmentLayout.segmentCount))
        self.nameLabel.setText(self.SegmentData.name + parentName)
        self.nameLabel.setAlignment(QtCore.Qt.AlignVCenter)

        self.limitLabel = QtWidgets.QLabel(self.segmentWidget)
        self.limitLabel.setGeometry(QtCore.QRect(
            0, h-20, SegmentLayout.limitLabelWidth, 20))
        self.limitLabel.setObjectName(
            "limitLabel_"+str(SegmentLayout.segmentCount))
        self.limitLabel.setText(
            str(self.SegmentData.base+self.SegmentData.length))

        SegmentLayout.segmentCount += 1
        SegmentLayout.nextY += h


class Ui_OutputWindow(object):
    def setupUi(self, OutputWindow, memory_data):
        OutputWindow.setObjectName("OutputWindow")
        OutputWindow.resize(300, 556)
        OutputWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.pushButton = QtWidgets.QPushButton(OutputWindow)
        self.pushButton.setGeometry(QtCore.QRect(104, 510, 92, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(OutputWindow)
        self.label.setGeometry(QtCore.QRect(121, 10, 58, 17))
        self.label.setObjectName("label")

        self.retranslateUi(OutputWindow)
        QtCore.QMetaObject.connectSlotsByName(OutputWindow)

        self.output_window = OutputWindow
        self.memory_data = memory_data

        self.MemoryInit()

    def retranslateUi(self, OutputWindow):
        _translate = QtCore.QCoreApplication.translate
        OutputWindow.setWindowTitle(_translate("OutputWindow", "Memory View"))
        self.pushButton.setText(_translate("OutputWindow", "Add Process"))
        self.label.setText(_translate("OutputWindow", "Memory"))

    def RefreshMemory(self):
        self.Memory.RefreshContainer(self.memory_data)

    def MemoryInit(self):
        self.Memory = MemoryLayout(self.memory_data, self.output_window)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    pro = Process()
    segments = [Segment("hole", 1000, 0, 0, True), Segment("Heap", 2000, pro, 1000, False), Segment(
        "hole", 15, 3000, 0, True), Segment("Stack", 1500, pro, 3015, False)]
    data = Memory(segments)
    data.processes.append(pro)
    ui.setupUi(OutputWindow, data)
    OutputWindow.show()
    sys.exit(app.exec_())
