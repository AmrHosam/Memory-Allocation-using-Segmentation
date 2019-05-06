import copy
import math
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
        if not self.free:
            segs = copy.copy(self.parentProcess.segments)
            segs.append(self)
            self.parentProcess.segments = segs

    def deallocate(self):
        if not self.free:
            self.parentProcess = "0"
            self.free = True
            self.name = "hole"

    def __eq__(self, seg):
        if self.free:
            if seg.free:
                return True
            return False
        return (str(self.name) == str(seg.name) and str(self.parentProcess.name) == str(seg.parentProcess.name))


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
            self.segments.append(segment)

    def allocate(self, process):

        # Amr: Add allocator algorithm here.

        # Amr: if process is added succesfully
        # self.processes.append(process)

        pass
    def compaction(self):
        compact = []
        next_base = 0
        hole_size = 0
        for mem_segment in self.segments:
            if(mem_segment.free):
                hole_size = hole_size + mem_segment.length
            else:
                mem_segment.base = next_base
                compact.append(mem_segment)
                next_base = next_base + mem_segment.length
        if(hole_size > 0):
            new_hole = Segment("hole", hole_size, 0, next_base, True)
            compact.append(new_hole)
        self.segments = copy.deepcopy(compact)

    def firstFit(self, process):
        temp_mem = copy.deepcopy(self.segments)
        success = False
        for pro_segment in process.segments:
            index = 0
            success = False
            for mem_segment in temp_mem:
                if(mem_segment.free and mem_segment.length >= pro_segment.length):
                    success = True
                    pro_segment.base = mem_segment.base
                    temp_mem.insert(index, pro_segment)
                    if(mem_segment.length > pro_segment.length):
                        new_hole = Segment("hole", mem_segment.length - pro_segment.length, 0, mem_segment.base + pro_segment.length, True)
                        temp_mem.insert(index+1, new_hole)
                        del temp_mem[index+2]
                    else:
                        del temp_mem[index+1]
                    break
                index += 1
            if(success == False):
                break
        if(success == True):
            self.segments = copy.deepcopy(temp_mem)
        return success

    def bestFit(self, process):
        temp_mem = copy.deepcopy(self.segments)
        success = False
        for pro_segment in process.segments:
            index = 0
            success = False
            mini = math.inf
            for i in range(0, len(temp_mem)):
                if(temp_mem[i].free and temp_mem[i].length >= pro_segment.length and temp_mem[i].length < mini):
                    index = i
                    mini = temp_mem[i].length
                    success = True
            if(success):
                pro_segment.base = temp_mem[index].base
                temp_mem.insert(index, pro_segment)
                if(temp_mem[index+1].length > pro_segment.length):
                    #print("aaaa")
                    new_hole = Segment("hole", temp_mem[index+1].length - pro_segment.length, 0, temp_mem[index+1].base + pro_segment.length, True)
                    temp_mem.insert(index+1, new_hole)
                    del temp_mem[index+2]
                else:
                    del temp_mem[index+1]
            else:
                break
        if(success == True):
            self.segments = copy.deepcopy(temp_mem)
        return success

    def worstFit(self, process):
        temp_mem = copy.deepcopy(self.segments)
        success = False
        for pro_segment in process.segments:
            index = 0
            success = False
            maxi = 0
            for i in range(0, len(temp_mem)):
                if(temp_mem[i].free and temp_mem[i].length >= pro_segment.length and temp_mem[i].length > maxi):
                    index = i
                    maxi = temp_mem[i].length
                    success = True
            if(success):
                pro_segment.base = temp_mem[index].base
                temp_mem.insert(index, pro_segment)
                if(temp_mem[index+1].length > pro_segment.length):
                    #print("aaaa")
                    new_hole = Segment("hole", temp_mem[index+1].length - pro_segment.length, 0, temp_mem[index+1].base + pro_segment.length, True)
                    temp_mem.insert(index+1, new_hole)
                    del temp_mem[index+2]
                else:
                    del temp_mem[index+1]
            else:
                break
        if(success == True):
            self.segments = copy.deepcopy(temp_mem)
        return success
    # def allocation(self,process):
    #     temp_mem = copy.deepcopy(self.segments)
    #     index = 0
    #     holes = []
    #     for segment in temp_mem:
    #         if(segment.free):
    #             holes.append([index, segment.length])
    #         index += 1
    #     for pro_segment in process.segments:
    #         success = False
    #         index = 0
    #         for index in range(0, len(holes)):
    #             print(holes[index][1])
    #             if(pro_segment.length <= temp_mem[holes[index][0]].length):
    #                 success = True
    #                 mem_segment = temp_mem[holes[index][0]]
    #                 pro_segment.base = mem_segment.base
    #                 temp_mem.insert(holes[index][0], pro_segment)
    #                 if(pro_segment.length < mem_segment.length):
    #                     new_hole = Segment("hole", mem_segment.length - pro_segment.length, 0, mem_segment.base + pro_segment.length, True)
    #                     temp_mem.insert(holes[index][0]+1, new_hole)
    #                     del temp_mem[holes[index][0]+2]
    #                     holes.insert(index, [holes[index][0]+1, mem_segment.length - pro_segment.length])
    #                     del holes[index+1]
    #                 else:
    #                     del temp_mem[holes[index][0]+1]
    #                     del holes[index]
    #                 break
    #         if(success == False):
    #             break
    #     #if(success == True):
    #     self.segments = copy.deepcopy(temp_mem)
    #     return success

    def deallocate(self, process):
        process.deallocate()
        i=0
        while i < (len(self.processes)):
            if self.processes[i].name == process.name:
                self.processes.remove(self.processes[i])
            i += 1
        del process  # possible bug
        prevSegment = Segment("a", 0, Process())
        Process.count -= 1
        prevSegment.parentProcess.name = "UT"
        i =0
        while i < (len(self.segments)):
            segment = self.segments[i]
            if segment == prevSegment:
                prevSegment.length += segment.length
                del self.segments[i]
                i -= 1
                segment = prevSegment
            prevSegment = segment
            i += 1
