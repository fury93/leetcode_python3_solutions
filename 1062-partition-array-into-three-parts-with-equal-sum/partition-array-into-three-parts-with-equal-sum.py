class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        S = sum(arr)
        if sum(arr) % 3:
            return False
        
        average, cnt, prefix = S // 3, 0, 0
        for n in arr:
            prefix += n
            if prefix == average:
                cnt +=1
                prefix = 0
            
        return cnt >= 3

