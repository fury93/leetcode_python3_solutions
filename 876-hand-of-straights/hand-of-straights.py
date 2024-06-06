class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)

        for val in sorted(cnt):
            if not cnt[val]: continue
            diff = cnt[val]
            for j in range(val, val + groupSize):
                if cnt[j] < diff:
                    return False
                cnt[j] -= diff

        return True