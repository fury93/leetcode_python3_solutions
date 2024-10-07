class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        def colToNumber(ch):
            return ord(ch) - 96
        
        return (colToNumber(c1[0]) + int(c1[1])) & 1 == colToNumber(c2[0]) + int(c2[1]) & 1