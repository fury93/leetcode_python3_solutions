class FrequencyTracker:

    def __init__(self):
        self.nums = [0] * (10**5 + 1) # frequency for the num
        self.freq = [0] * (10**5 + 1) # count of nums with such freq

    def add(self, number: int) -> None:
        numFreq = self.nums[number]
        if numFreq > 0:
            self.freq[numFreq] -= 1
        self.nums[number] += 1
        self.freq[numFreq + 1] += 1

    def deleteOne(self, number: int) -> None:
        numFreq = self.nums[number]
        if not numFreq: return
        self.freq[numFreq] -= 1
        self.nums[number] -= 1
        self.freq[numFreq - 1] += 1

        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)