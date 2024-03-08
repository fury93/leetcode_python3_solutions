class FrequencyBlock(object):
    def __init__(self, freq = 0):
        self.freq = freq
        self.totalCnt = 0
        self.prev = None
        self.next = None

    def removeNum(self):
        self.totalCnt -= 1
    
    def addNum(self):
        self.totalCnt += 1

    def empty(self):
        return self.totalCnt == 0
    
    def frequency(self):
        return self.freq

    def totalFrequency(self) -> int:
        return self.totalCnt * self.freq

    def insertAfter(self, new_block):
        new_block.next = self.next
        new_block.prev = self
        self.next.prev = new_block
        self.next = new_block

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None

class Solution:
    def __init__(self):
        self.start = FrequencyBlock()
        self.end = FrequencyBlock()
        self.start.next = self.end
        self.end.prev = self.start
        self.mapping = {} # mapping num to frequency block

    def maxFrequencyElements(self, nums: List[int]) -> int:
        for n in nums:
            if n in self.mapping:
                current_block = self.mapping[n]
                current_block.removeNum()
            else:
                 current_block = self.start
                
            new_frequency = current_block.frequency() + 1

            if new_frequency != current_block.next.frequency():
                # create new frequency block
                next_block = FrequencyBlock(new_frequency)
                current_block.insertAfter(next_block)
            else:
                next_block = current_block.next

            next_block.addNum()
            self.mapping[n] = next_block

            # remove current block if it's emtpy and not dummy
            if current_block.frequency() != 0 and current_block.empty():
                current_block.remove()

            cur = self.start
            while cur:
                cur = cur.next

        return self.end.prev.totalFrequency()     

class FrequencyBlock2(object):
    def __init__(self, freq = 0):
        self.freq = freq
        self.nums = set()
        self.prev = None
        self.next = None

    def removeNum(self, num):
        self.nums.remove(num)
    
    def addNum(self, num):
        self.nums.add(num)

    def empty(self):
        return len(self.nums) == 0
    
    def frequency(self):
        return self.freq

    def totalFrequency(self) -> int:
        return len(self.nums) * self.freq

    def insertAfter(self, new_block):
        new_block.next = self.next
        new_block.prev = self
        self.next.prev = new_block
        self.next = new_block

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None

class Solution2:
    def __init__(self):
        self.start = FrequencyBlock()
        self.end = FrequencyBlock()
        self.start.next = self.end
        self.end.prev = self.start
        self.mapping = {} # mapping num to frequency block

    def maxFrequencyElements(self, nums: List[int]) -> int:
        for n in nums:
            if n in self.mapping:
                current_block = self.mapping[n]
                current_block.removeNum(n)
            else:
                 current_block = self.start
                

            new_frequency = current_block.freq + 1
            if new_frequency != current_block.next.frequency():
                # create new frequency block
                new_block = FrequencyBlock(new_frequency)
                current_block.insertAfter(new_block)
            else:
                new_block = current_block.next

            new_block.addNum(n)
            self.mapping[n] = new_block

            # remove current block if it's emtpy and not dummy
            if current_block.frequency() != 0 and current_block.empty():
                current_block.remove()

        return self.end.prev.totalFrequency()

        