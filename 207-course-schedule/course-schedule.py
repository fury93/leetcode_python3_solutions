class Solution:
    def canFinish(self, n, prerequisites):
        adj, rank = [[] for _ in range(n)], [0] * n
        
        for child, parent in prerequisites:
            adj[parent].append(child)
            rank[child] += 1

        visited = 0
        q = deque(i for i in range(n) if rank[i] == 0)
        
        while q:
            course = q.popleft()
            visited += 1

            for nextCourse in adj[course]:
                rank[nextCourse] -= 1
                if rank[nextCourse] == 0:
                    q.append(nextCourse)

        return visited == n