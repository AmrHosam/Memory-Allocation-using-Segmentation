class Segment:
    def __init__(self, name, length, parent_process, base=-1, free=False):
        self.parentProcess = parent_process
        self.base = base
        self.length = length
        self.free = free
        self.name = name

    def reset(self, base, length, free, name):
        self.base = base
        self.length = length
        self.free = free
        self.name = name

    def deallocate(self):
        self.free = True
        self.name = "hole"


class Process:
    def __init__(self, segments):
        self.segments = []
        for segment in segments:
            self.segments.append(segment)

    def deallocate(self):
        for segment in self.segments:
            segment.deallocate()
