class Solution:
    def numberOfAlternatingGroups(self, col: List[int]) -> int:
        col.extend(col[:2]) # add first two symbols to the end
        return sum(col[i] == col[i+2] != col[i+1] for i in range(len(col)-2))