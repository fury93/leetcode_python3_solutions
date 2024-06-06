class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        values = sorted(cnt.keys())

        for i in range(len(values)):
            val = values[i]
            if not cnt[val]: continue
            diff = cnt[val]
            for j in range(val, val + groupSize):
                if cnt[j] < diff:
                    return False
                cnt[j] -= diff

        return True