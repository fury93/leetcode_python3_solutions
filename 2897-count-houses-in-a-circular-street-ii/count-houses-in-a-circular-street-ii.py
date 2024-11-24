# Definition for a street.
# class Street:
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:

        def period() -> int:
            pattern = []
            for _ in range(2*k):
                pattern.append(street.isDoorOpen())
                street.moveRight()

            # KMP algorithm
            kmp, ptr = [0], 0
            for i in range(1,2*k):
                while ptr and pattern[i] != pattern[ptr]:
                    ptr = kmp[ptr-1]
                if pattern[i] == pattern[ptr]:
                    ptr += 1
                kmp.append(ptr)

            # The shortest period is 2k minus the longest match at the end
            return 2*k - ptr

        prd1 = period()

        while not street.isDoorOpen():
            street.moveRight()
        street.closeDoor()

        prd2 = period()

        # Least common multiple
        return lcm(prd1, prd2)