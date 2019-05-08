import random
from MemoryObjects import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MemoryLayout:

    def __init__(self, data, window):
        self.window = window
        self.segments = []
        self.MemData = []
        self.MemData = copy.deepcopy(data)
        lastSegment = self.MemData.segments[len(self.MemData.segments)-1]
        self.totalLocationsNum = lastSegment.base + lastSegment.length + 1
        self.SegContainerHeight = 700
        self.SegContainerMinWidth = 160
        self.ratio = self.SegContainerHeight / self.totalLocationsNum

        self.MemoryScroll = QtWidgets.QScrollArea(self.window.output_window)
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
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
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
        self.SegmentsContainer.setMinimumSize(
            QtCore.QSize(self.SegContainerMinWidth, self.SegContainerHeight))
        self.SegmentsContainer.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.SegmentsContainer.setObjectName("SegmentsContainer")
        self.SegsContLayout = QtWidgets.QVBoxLayout(self.SegmentsContainer)
        self.SegsContLayout.setContentsMargins(0, 0, 0, 0)
        self.SegsContLayout.setSpacing(0)
        self.SegsContLayout.setObjectName("SegsContLayout")

        self.__AddContents(window)
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.SegmentsContainer.setMinimumSize(
            QtCore.QSize(self.SegContainerMinWidth, self.SegContainerHeight))
        self.SegmentsContainer.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.scrollAreaWidgetLayout.addWidget(self.SegmentsContainer)

        self.MemoryScroll.setWidget(self.scrollAreaWidgetContents)
        window.WindowContainerLayout.addWidget(self.MemoryScroll)

    def RefreshContainer(self, data, window):
        SegmentLayout.segmentCount = 0
        self.SegContainerHeight = 700
        lastSegment = self.MemData.segments[len(self.MemData.segments)-1]
        self.totalLocationsNum = lastSegment.base + lastSegment.length + 1
        self.ratio = self.SegContainerHeight / self.totalLocationsNum

        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.SegmentsContainer.setMinimumSize(
            QtCore.QSize(self.SegContainerMinWidth, self.SegContainerHeight))
        self.SegmentsContainer.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))

        self.MemData.segments.clear()
        self.MemData.processes.clear()
        self.segments.clear()
        del self.MemData
        del self.segments

        self.segments = []
        self.MemData = []
        self.MemData = copy.deepcopy(data)

        item = self.SegsContLayout.takeAt(0)
        while item:
            w = item.widget()
            w.setParent(None)
            del w
            del item
            item = self.SegsContLayout.takeAt(0)

        self.__AddContents(window)
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.SegmentsContainer.setMinimumSize(
            QtCore.QSize(self.SegContainerMinWidth, self.SegContainerHeight))
        self.SegmentsContainer.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))
        self.scrollAreaWidgetContents.setMaximumSize(
            QtCore.QSize(500, self.SegContainerHeight))

    def __AddContents(self, window):
        SegmentLayout.segmentCount = 0
        for segment in self.MemData.segments:
            segment_layout = SegmentLayout(self, segment)
            self.segments.append(segment_layout)

            segment_layout.segmentWidget.mouseDoubleClickEvent = self.make_deallocate(
                segment, self)

    def make_deallocate(self, Segment, Memory):
        def deallocate(self):
            if Segment.free:
                return
            Memory.MemData.deallocate(Segment.parentProcess)
            data = copy.deepcopy(Memory.MemData)
            Memory.RefreshContainer(data, Memory.window)
        return deallocate


class SegmentLayout:
    segmentMinWidth = 160
    minSegmentHeight = 20
    segmentCount = 0
    holeColor = "rgb(155, 155, 155)"

    def __init__(self, memory_layout, segment):  # edit here
        color = []
        color.append(random.randrange(120, 256))
        color.append(random.randrange(120, 256))
        color.append(random.randrange(120, 256))
        i = random.randrange(0, 3)
        color[i] = 0
        self.color = "rgb("+str(color[0]) + ", " + \
            str(color[1]) + ", "+str(color[2]) + ")"
        if segment.free:
            self.color = SegmentLayout.holeColor
            parentName = ""
        else:
            parentName = " ("+segment.parentProcess.name+")"

        self.SegmentData = segment

        h = int(memory_layout.ratio * self.SegmentData.length)
        if h < SegmentLayout.minSegmentHeight:
            memory_layout.SegContainerHeight += SegmentLayout.minSegmentHeight - h
            h = SegmentLayout.minSegmentHeight

        if SegmentLayout.segmentCount == 0:
            if h < 40:
                memory_layout.SegContainerHeight += 40 - h
                h = 40

        self.segmentWidget = QtWidgets.QWidget(
            memory_layout.SegmentsContainer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.segmentWidget.sizePolicy().hasHeightForWidth())

        self.segmentWidget.setSizePolicy(sizePolicy)
        self.segmentWidget.setMinimumSize(
            QtCore.QSize(SegmentLayout.segmentMinWidth, h))
        self.segmentWidget.setMaximumSize(QtCore.QSize(16777215, h))
        self.segmentWidget.setObjectName(
            "segment_"+str(SegmentLayout.segmentCount))
        self.segmentWidget.setStyleSheet(
            "background-color: "+self.color+";")

        self.segmentLayout = QtWidgets.QHBoxLayout(self.segmentWidget)
        self.segmentLayout.setContentsMargins(0, 0, 0, 0)
        self.segmentLayout.setSpacing(0)
        self.segmentLayout.setObjectName(
            "segment"+str(SegmentLayout.segmentCount)+"Layout")

        if SegmentLayout.segmentCount == 0:
            self.firstSegContainer = QtWidgets.QWidget(self.segmentWidget)
            self.firstSegContainer.setMaximumSize(
                QtCore.QSize(self.segmentMinWidth, 16777215))
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
            self.zero.setMaximumSize(QtCore.QSize(
                self.segmentMinWidth, h))
            self.zero.setAlignment(QtCore.Qt.AlignLeading |
                                   QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.zero.setObjectName("zero")
            self.zero.setText("0")
            self.limitLabel = QtWidgets.QLabel(self.firstSegContainer)
            self.limitLabel.setGeometry(QtCore.QRect(0, h-18, 121, 17))
            self.limitLabel.setMaximumSize(QtCore.QSize(160, h))
            self.limitLabel.setAlignment(
                QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
            self.limitLabel.setObjectName(
                "limitLabel"+str(SegmentLayout.segmentCount))
            self.limitLabel.setText(
                str(self.SegmentData.base+self.SegmentData.length))
            self.segmentLayout.addWidget(self.firstSegContainer)
        else:
            self.limitLabel = QtWidgets.QLabel(self.segmentWidget)
            self.limitLabel.setMaximumSize(QtCore.QSize(160, h))
            self.limitLabel.setVisible(True)
            self.limitLabel.setAlignment(
                QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
            self.limitLabel.setObjectName(
                "limitLabel"+str(SegmentLayout.segmentCount))
            self.limitLabel.setText(
                str(self.SegmentData.base+self.SegmentData.length))
            self.segmentLayout.addWidget(self.limitLabel)
        self.nameLabel = QtWidgets.QLabel(self.segmentWidget)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName(
            "nameLabel"+str(SegmentLayout.segmentCount))
        self.nameLabel.setText(self.SegmentData.name + parentName +
                               ": " + str(self.SegmentData.length))

        self.segmentLayout.addWidget(self.nameLabel)

        memory_layout.SegsContLayout.addWidget(self.segmentWidget)

        SegmentLayout.segmentCount += 1
