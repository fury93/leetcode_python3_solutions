class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q1, q2 = set(), collections.deque(range(10))
        while q2:
            n = q2.popleft()
            if low <= n <= high:
                q1.add(n)
            if n < high:
                d = n % 10
                if d == 0:
                    q2.append(n * 10 + 1)
                elif d == 9:
                    q2.append(n * 10 + 8)
                else:
                    q2.append(n * 10 + d + 1)
                    q2.append(n * 10 + d - 1)
        return sorted(q1)