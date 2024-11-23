class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        def taxi(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])
        
        S = sum(2 * taxi(tree, nut) for nut in nuts)
        return min(S + taxi(squirrel, nut) - taxi(nut, tree) for nut in nuts)