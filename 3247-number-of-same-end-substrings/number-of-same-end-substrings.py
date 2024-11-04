class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        res,  ln = [0] * len(queries), len(s)
        symbolFreq = [[0] * ln for _ in range(26)]
        for i, ch in enumerate(s):
            symbolFreq[ord(ch) - 97][i] = 1
        
        # generate prefix sum without initial 0 => [1,2,3,4] => [1,3,6,10]
        # itertools.accumulate(nums, initial=0) => [1,2,3,4] => [0, 1, 3, 6, 10]
        for freq in symbolFreq:
            for i in range(1, ln):
                freq[i] += freq[i-1]

        for i, (start, end) in enumerate(queries):
            allSubstrings = 0
            for freq in symbolFreq:
                freqEnd = freq[end]
                freqStart = 0 if start == 0 else freq[start-1]
                symbolCnt = freqEnd - freqStart
                if symbolCnt > 0:
                    allSubstrings += (symbolCnt * (symbolCnt + 1)) // 2

            res[i] = allSubstrings

        return res