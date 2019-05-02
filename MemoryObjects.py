import copy


class Segment:  # this class should be used by Allocator and Deallocator

    # base parameter should be set only by the Allocator Algorithm. free parameter should be set only by Deallocator Algorithm
    def __init__(self, name, length, parent_process, base=-1, free=False):
        self.parentProcess = parent_process
        self.base = copy.deepcopy(base)
        self.length = copy.deepcopy(length)
        self.free = copy.deepcopy(free)
        self.name = copy.deepcopy(name)

    def deallocate(self):
        self.parentProcess = 0
        self.free = True
        self.name = "hole"

    def __eq__(self, seg):
        return (self.name == seg.name and self.parentProcess.name == seg.parentProcess.name)


class Process:  # this class should only be used by Deallocator
    count = 0

    def __init__(self):
        self.name = "UT"+str(Process.count)
        Process.count += 1
        self.segments = []

    def addSegments(self, segments):
        for segment in segments:
            self.segments.append(segment)

    def deallocate(self):
        for segment in self.segments:
            segment.deallocate()


class Memory:
    def __init__(self, segments):
        self.segments = []
        for segment in segments:
            self.segments.append(copy.deepcopy(segment))

    def allocate(self, segment):
        # Amr
        pass

    def deallocate(self, process):
        process.deallocate()
        prevSegment = Segment("a", 0, Process())
        Process.count -= 1
        prevSegment.parentProcess.name = "UT"
        i = 0
        for segment in self.segments:
            if segment == prevSegment:
                prevSegment.length += segment.length
                self.segments.remove(segment)
                segment = prevSegment
            prevSegment = segment
            i += 1
