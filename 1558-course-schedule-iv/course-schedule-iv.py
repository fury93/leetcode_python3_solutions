class Solution:
    def checkIfPrerequisite(
        self,
        N: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        isPrerequisite = [[False] * N for _ in range(N)]

        for u, v in prerequisites:
            isPrerequisite[u][v] = True

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if not isPrerequisite[i][j]:
                        isPrerequisite[i][j] = isPrerequisite[i][k] and isPrerequisite[k][j]

        return [isPrerequisite[u][v] for u, v in queries]