# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testview.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutputWindow(object):
    def setupUi(self, OutputWindow):
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

        self.MemoryScroll = QtWidgets.QScrollArea(OutputWindow)
        self.MemoryScroll.setMinimumSize(QtCore.QSize(181, 100))
        self.MemoryScroll.setWidgetResizable(True)
        self.MemoryScroll.setAlignment(QtCore.Qt.AlignCenter)
        self.MemoryScroll.setObjectName("MemoryScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 415, 350))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.scrollAreaWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaWidgetLayout.setSpacing(0)
        self.scrollAreaWidgetLayout.setObjectName("scrollAreaWidgetLayout")
        self.SegmentsContainer = QtWidgets.QWidget(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SegmentsContainer.sizePolicy().hasHeightForWidth())
        self.SegmentsContainer.setSizePolicy(sizePolicy)
        self.SegmentsContainer.setMinimumSize(QtCore.QSize(160, 222))
        self.SegmentsContainer.setMaximumSize(QtCore.QSize(16777215, 222))
        self.SegmentsContainer.setObjectName("SegmentsContainer")
        self.SegsContLayout = QtWidgets.QVBoxLayout(self.SegmentsContainer)
        self.SegsContLayout.setContentsMargins(0, 0, 0, 0)
        self.SegsContLayout.setSpacing(0)
        self.SegsContLayout.setObjectName("SegsContLayout")
        self.FirstSegmentHeap = QtWidgets.QWidget(self.SegmentsContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FirstSegmentHeap.sizePolicy().hasHeightForWidth())
        self.FirstSegmentHeap.setSizePolicy(sizePolicy)
        self.FirstSegmentHeap.setMinimumSize(QtCore.QSize(160, 79))
        self.FirstSegmentHeap.setMaximumSize(QtCore.QSize(16777215, 79))
        self.FirstSegmentHeap.setObjectName("FirstSegmentHeap")
        self.FirstSegLayout = QtWidgets.QHBoxLayout(self.FirstSegmentHeap)
        self.FirstSegLayout.setContentsMargins(0, 0, 0, 0)
        self.FirstSegLayout.setSpacing(0)
        self.FirstSegLayout.setObjectName("FirstSegLayout")
        self.firstSegContainer = QtWidgets.QWidget(self.FirstSegmentHeap)
        self.firstSegContainer.setMaximumSize(QtCore.QSize(160, 16777215))
        self.firstSegContainer.setObjectName("firstSegContainer")
        self.zero = QtWidgets.QLabel(self.firstSegContainer)
        self.zero.setGeometry(QtCore.QRect(0, 0, 121, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setMaximumSize(QtCore.QSize(160, 16777215))
        self.zero.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.zero.setObjectName("zero")
        self.HeapLimit = QtWidgets.QLabel(self.firstSegContainer)
        self.HeapLimit.setGeometry(QtCore.QRect(0, 60, 121, 17))
        self.HeapLimit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.HeapLimit.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.HeapLimit.setObjectName("HeapLimit")
        self.FirstSegLayout.addWidget(self.firstSegContainer)
        self.HeapLabel = QtWidgets.QLabel(self.FirstSegmentHeap)
        self.HeapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HeapLabel.setObjectName("HeapLabel")
        self.FirstSegLayout.addWidget(self.HeapLabel)
        self.SegsContLayout.addWidget(self.FirstSegmentHeap)
        self.SecondSegment = QtWidgets.QWidget(self.SegmentsContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SecondSegment.sizePolicy().hasHeightForWidth())
        self.SecondSegment.setSizePolicy(sizePolicy)
        self.SecondSegment.setMinimumSize(QtCore.QSize(160, 79))
        self.SecondSegment.setMaximumSize(QtCore.QSize(16777215, 79))
        self.SecondSegment.setObjectName("SecondSegment")
        self.SecondSegLayout = QtWidgets.QHBoxLayout(self.SecondSegment)
        self.SecondSegLayout.setContentsMargins(0, 0, 0, 0)
        self.SecondSegLayout.setSpacing(0)
        self.SecondSegLayout.setObjectName("SecondSegLayout")
        self.StackLimit = QtWidgets.QLabel(self.SecondSegment)
        self.StackLimit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.StackLimit.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.StackLimit.setObjectName("StackLimit")
        self.SecondSegLayout.addWidget(self.StackLimit)
        self.StackLabel = QtWidgets.QLabel(self.SecondSegment)
        self.StackLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StackLabel.setObjectName("StackLabel")
        self.SecondSegLayout.addWidget(self.StackLabel)
        self.SegsContLayout.addWidget(self.SecondSegment)
        self.ThirdSegment = QtWidgets.QWidget(self.SegmentsContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ThirdSegment.sizePolicy().hasHeightForWidth())
        self.ThirdSegment.setSizePolicy(sizePolicy)
        self.ThirdSegment.setMinimumSize(QtCore.QSize(160, 30))
        self.ThirdSegment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ThirdSegment.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.ThirdSegment.setObjectName("ThirdSegment")
        self.ThirdSegLayout = QtWidgets.QHBoxLayout(self.ThirdSegment)
        self.ThirdSegLayout.setContentsMargins(0, 0, 0, 0)
        self.ThirdSegLayout.setSpacing(0)
        self.ThirdSegLayout.setObjectName("ThirdSegLayout")
        self.DataLimit = QtWidgets.QLabel(self.ThirdSegment)
        self.DataLimit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.DataLimit.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.DataLimit.setObjectName("DataLimit")
        self.ThirdSegLayout.addWidget(self.DataLimit)
        self.DataLabel = QtWidgets.QLabel(self.ThirdSegment)
        self.DataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DataLabel.setObjectName("DataLabel")
        self.ThirdSegLayout.addWidget(self.DataLabel)
        self.SegsContLayout.addWidget(self.ThirdSegment)
        self.FourthSegment = QtWidgets.QWidget(self.SegmentsContainer)
        self.FourthSegment.setMinimumSize(QtCore.QSize(160, 30))
        self.FourthSegment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.FourthSegment.setStyleSheet(
            "background-color: rgb(233, 185, 110);")
        self.FourthSegment.setObjectName("FourthSegment")
        self.FourthSegLayout = QtWidgets.QHBoxLayout(self.FourthSegment)
        self.FourthSegLayout.setContentsMargins(0, 0, 0, 0)
        self.FourthSegLayout.setSpacing(0)
        self.FourthSegLayout.setObjectName("FourthSegLayout")
        self.TextLimit = QtWidgets.QLabel(self.FourthSegment)
        self.TextLimit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.TextLimit.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.TextLimit.setObjectName("TextLimit")
        self.FourthSegLayout.addWidget(self.TextLimit)
        self.TextLabel = QtWidgets.QLabel(self.FourthSegment)
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setObjectName("TextLabel")
        self.FourthSegLayout.addWidget(self.TextLabel)
        self.SegsContLayout.addWidget(self.FourthSegment)
        self.scrollAreaWidgetLayout.addWidget(self.SegmentsContainer)
        self.MemoryScroll.setWidget(self.scrollAreaWidgetContents)
        self.WindowContainerLayout.addWidget(self.MemoryScroll)
        self.AddBtn = QtWidgets.QPushButton(OutputWindow)
        self.AddBtn.setMaximumSize(QtCore.QSize(180, 16777215))
        self.AddBtn.setObjectName("AddBtn")
        self.WindowContainerLayout.addWidget(
            self.AddBtn, 0, QtCore.Qt.AlignHCenter)
        self.OutputWindowLayout.addLayout(self.WindowContainerLayout)

        self.retranslateUi(OutputWindow)
        QtCore.QMetaObject.connectSlotsByName(OutputWindow)

    def retranslateUi(self, OutputWindow):
        _translate = QtCore.QCoreApplication.translate
        OutputWindow.setWindowTitle(_translate("OutputWindow", "Memory View"))
        self.TitleLabel.setText(_translate("OutputWindow", "Memory"))
        self.zero.setText(_translate("OutputWindow", "0"))
        self.HeapLimit.setText(_translate("OutputWindow", "100"))
        self.HeapLabel.setText(_translate("OutputWindow", "HEAP"))
        self.StackLimit.setText(_translate("OutputWindow", "200"))
        self.StackLabel.setText(_translate("OutputWindow", "Stack"))
        self.DataLimit.setText(_translate("OutputWindow", "250"))
        self.DataLabel.setText(_translate("OutputWindow", "Data"))
        self.TextLimit.setText(_translate("OutputWindow", "300"))
        self.TextLabel.setText(_translate("OutputWindow", "Text"))
        self.AddBtn.setText(_translate("OutputWindow", "Add Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputWindow = QtWidgets.QWidget()
    ui = Ui_OutputWindow()
    ui.setupUi(OutputWindow)
    OutputWindow.show()
    sys.exit(app.exec_())
