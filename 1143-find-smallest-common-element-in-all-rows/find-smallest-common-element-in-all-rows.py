class Solution:
    def smallestCommonElement(self, M):
        c = collections.Counter()
        for row in M:
            for a in row:
                c[a] += 1
                if c[a] == len(M):
                    return a
        return -1