class Solution:
    def pourWater(self, heights, V, K):
        for _ in range(V):
            index = -1
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    index = i
            if index != -1:
                heights[index] += 1
                continue

            index = -1
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    index = i
            if index != -1:
                heights[index] += 1
            else:
                heights[K] += 1
        return heights