class FrequencyBlock(object):
    def __init__(self, freq = 0):
        self.freq = freq
        self.nums = set()
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev, self.next = None, None
        # del self

    def remove_num(self, num):
        self.nums.remove(num)
    
    def add_num(self, num):
        self.nums.add(num)

    def empty(self):
        return len(self.nums) == 0
    
    def frequency(self):
        return self.freq

    def total_frequency(self) -> int:
        return len(self.nums) * self.freq

    def insert_after(self, new_block):
        new_block.next = self.next
        new_block.prev = self
        self.next.prev = new_block
        self.next = new_block

class Solution:
    def __init__(self):
        self.start = FrequencyBlock()
        self.end = FrequencyBlock()
        self.start.next = self.end
        self.end.prev = self.start
        self.mapping = {} # mapping num to frequency block

    def maxFrequencyElements(self, nums: List[int]) -> int:
        for n in nums:
            if not n in self.mapping:
                current_block = self.start
            else:
                current_block = self.mapping[n]
                current_block.remove_num(n)

            new_frequency = current_block.freq + 1
            print(n, current_block.freq, current_block.next)
            if new_frequency != current_block.next.frequency():
                # create new frequency block
                new_block = FrequencyBlock(new_frequency)
                current_block.insert_after(new_block)
            else:
                new_block = current_block.next

            new_block.add_num(n)
            self.mapping[n] = new_block

            # remove current block if it's emtpy and not dummy
            #if not current_block.empty() and current_block.frequency() != 0:
                #current_block.remove()

        return self.end.prev.total_frequency()

        