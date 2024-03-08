class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        for m, n in zip(messages, senders):
            d[n] += len(m.split())
        
        return max(d, key = lambda k: (d[k], k))