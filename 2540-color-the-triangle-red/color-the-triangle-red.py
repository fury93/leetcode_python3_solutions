class Solution:
    def colorRed(self, n: int) -> List[List[int]]:
        a = [[1, 1]]
        for i, start, short in zip(range(n, 1, -1), cycle((1, 2, 3, 1)), cycle((0, 1))):
            for j in range(start, i * 2, 2):
                a.append([i, j])
                if short:
                    break
        return a