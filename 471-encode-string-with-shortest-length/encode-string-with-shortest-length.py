class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        i=(s+s).find(s,1)
        encoded=str(len(s)//i)+'['+self.encode(s[:i])+']' if i<len(s) else s
        splitEncoded=[self.encode(s[:i])+self.encode(s[i:]) for i in range(1,len(s))]
        return min(splitEncoded+[encoded],key=len)