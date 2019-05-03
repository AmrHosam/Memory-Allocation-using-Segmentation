import copy
import math
# hole0 = Segment("hole", 1400, 0, 0, True)
# seg0 = Segment("seg0", 1000, 0, 1400, False)
# hole1 = Segment("hole", 800, 0, 2400, True)
# seg3 = Segment("seg3", 1100, 0, 3200, False)
# seg2 = Segment("seg2", 400, 0, 4300, False)
# seg4 = Segment("seg4", 1000, 0, 4700, False)
# hole2 = Segment("hole", 600, 0, 5700, True)
# seg1 = Segment("seg1", 400, 0, 6300, False)
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
# mem_segments = [Segment("hole", 1400, 0, 0, True), Segment("seg0", 1000, 0, 1400, False), Segment("hole", 800, 0, 2400, True), Segment("seg3", 1100, 0, 3200, False), 
# Segment("seg2", 400, 0, 4300, False), Segment("seg4", 1000, 0, 4700, False), Segment("hole", 600, 0, 5700, True), Segment("seg1", 400, 0, 6300, False)]
# mem = Memory(mem_segments)
# pro_segments = [Segment("PS0", 500, 0), Segment("PS1", 500, 0), Segment("PS2", 100, 0)]
# pro = Process()
# pro.addSegments(pro_segments)
# output = []
# res = mem.worstFit(pro)
# print(res)
# for segment in mem.segments:
#     print(segment.name+"    "+str(segment.base)+"   "+str(segment.length))