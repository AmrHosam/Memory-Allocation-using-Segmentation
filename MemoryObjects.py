import copy

# The third window (segments window) creates a parent process and its segments, then calls the allocator method.
# The Segment window should return the new memory object.


class Segment:  # this class should be used by Allocator and Deallocator

    # before creating a segment a parent process must be created. In the segments window only one new process should be created
    # constructor automatically appends the new segment to the parent process's list of segments
    # base parameter should be set only by the Allocator Algorithm. free parameter should be set only by Deallocator Algorithm
    def __init__(self, name, length, parent_process, base=-1, free=False):
        self.parentProcess = parent_process
        self.base = copy.deepcopy(base)
        self.length = copy.deepcopy(length)
        self.free = copy.deepcopy(free)
        self.name = copy.deepcopy(name)
        self.parentProcess.segments.append(self)

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

    def deallocate(self):
        for segment in self.segments:
            segment.deallocate()


class Memory:
    def __init__(self, segments):
        # List that holds all segments of Memory
        self.segments = []

        # List that holds all (newly) allocated processes in Memory
        self.processes = []

        for segment in segments:
            self.segments.append(copy.deepcopy(segment))

    def allocate(self, process):

        # Amr: Add allocator algorithm here.

        # Amr: if process is added succesfully
        # self.processes.append(process)

        pass

    def deallocate(self, process):
        process.deallocate()
        self.processes.remove(process)
        del process  # possible bug
        prevSegment = Segment("a", 0, Process())
        Process.count -= 1
        prevSegment.parentProcess.name = "UT"
        # i = 0
        for segment in self.segments:
            if segment == prevSegment:
                prevSegment.length += segment.length
                self.segments.remove(segment)
                segment = prevSegment
            prevSegment = segment
            # i += 1
