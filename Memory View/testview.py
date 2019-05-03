# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemoryView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MemoryObjects import *
import random


class Ui_OutputWindow(object):
    def setupUi(self, OutputWindow):
        OutputWindow.setObjectName("OutputWindow")
        OutputWindow.resize(300, 556)
        OutputWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.pushButton = QtWidgets.QPushButton(OutputWindow)
        self.pushButton.setGeometry(QtCore.QRect(104, 510, 92, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(OutputWindow)
        self.label.setGeometry(QtCore.QRect(121, 10, 58, 17))
        self.label.setObjectName("label")
        #
        self.scrollArea = QtWidgets.QScrollArea(OutputWindow)
        self.scrollArea.setGeometry(QtCore.QRect(70, 130, 181, 200))
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        #
        #
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 165, 220))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #
        #
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setGeometry(QtCore.QRect(0, 160, 165, 30))
        self.widget_3.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(65, 0, 100, 30))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 60, 20))
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 165, 80))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(65, 0, 100, 80))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 60, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 60, 20))
        self.label_4.setObjectName("label_4")
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setGeometry(QtCore.QRect(0, 190, 165, 30))
        self.widget_4.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.widget_4.setObjectName("widget_4")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setGeometry(QtCore.QRect(65, 0, 100, 30))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 60, 20))
        self.label_10.setObjectName("label_10")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(0, 80, 165, 80))
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(65, 0, 100, 80))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(0, 60, 60, 20))
        self.label_7.setObjectName("label_7")
        #
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(OutputWindow)
        QtCore.QMetaObject.connectSlotsByName(OutputWindow)

    def retranslateUi(self, OutputWindow):
        _translate = QtCore.QCoreApplication.translate
        OutputWindow.setWindowTitle(_translate("OutputWindow", "Memory View"))
        self.pushButton.setText(_translate("OutputWindow", "Add Process"))
        self.label.setText(_translate("OutputWindow", "Memory"))
        #
        self.label_6.setText(_translate("OutputWindow", "HEAP"))
        self.label_8.setText(_translate("OutputWindow", "250"))
        self.label_2.setText(_translate("OutputWindow", "HEAP"))
        self.label_3.setText(_translate("OutputWindow", "0"))
        self.label_4.setText(_translate("OutputWindow", "100"))
        self.label_9.setText(_translate("OutputWindow", "HEAP"))
        self.label_10.setText(_translate("OutputWindow", "300"))
        self.label_5.setText(_translate("OutputWindow", "HEAP"))
        self.label_7.setText(_translate("OutputWindow", "200"))
        #

    def addSegment(self, y, h):
        pass

    def MemoryInit(self):

        self.segmets = []


class MemoryLayout:
    Height = 450
    Width = 181
    X = 60
    Y = 40

    def __init__(self, data):
        self.segments = []
        self.MemData = []
        self.MemData = copy.deepcopy(data)
        lastSegment = self.MemData.segments[len(self.MemData.segments)-1]
        self.totalLocationsNum = lastSegment.base + lastSegment.length + 1
        self.ratio = 900 / self.totalLocationsNum

        self.scrollArea = QtWidgets.QScrollArea(OutputWindow)
        self.scrollArea.setGeometry(QtCore.QRect(
            MemoryLayout.X, MemoryLayout.Y, MemoryLayout.Width, MemoryLayout.Height))
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("MemoryLayout")

        self.WidgetContainer = QtWidgets.QWidget()
        self.WidgetContainer.setGeometry(QtCore.QRect(0, 0, 165, 900))
        self.WidgetContainer.setObjectName("WidgetContainer")
        self.containerHeight = 900

    def RefreshContainer(self, data):
        self.MemData.clear()
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
        self.containerHeight = 900
        self.AddContents()

    def AddContents(self):
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
        self.nameLabel.setText(self.SegmentData.name +
                               "\n(" + self.SegmentData.parentProcess.name + ")")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.limitLabel = QtWidgets.QLabel(self.segmentWidget)
        self.limitLabel.setGeometry(QtCore.QRect(
            0, h-20, SegmentLayout.limitLabelWidth, 20))
        self.limitLabel.setObjectName(
            "limitLabel_"+str(SegmentLayout.segmentCount))
        self.limitLabel.setText(str(y+h))

        SegmentLayout.segmentCount += 1
        SegmentLayout.nextY += h


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    ui.setupUi(OutputWindow)
    OutputWindow.show()
    sys.exit(app.exec_())
