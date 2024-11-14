class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0
        self.n4 = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.i4 == self.n4:
                self.i4 = 0
                self.n4 = read4(self.buf4)
                if self.n4 == 0:
                    break
            buf[i] = self.buf4[self.i4]
            self.i4 += 1
            i += 1
        return i