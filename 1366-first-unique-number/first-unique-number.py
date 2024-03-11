class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = deque()
        self.uniqNums = dict()
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while self.nums and not self.uniqNums[self.nums[0]]:
            self.nums.popleft()

        return self.nums[0] if self.nums else -1

    def add(self, value: int) -> None:
        if value in self.uniqNums:
            self.uniqNums[value] = False
        else:
            self.uniqNums[value] = True
            self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)