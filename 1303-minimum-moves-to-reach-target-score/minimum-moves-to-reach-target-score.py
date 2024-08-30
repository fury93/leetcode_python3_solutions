class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while target > 1:
            if maxDoubles == 0: break

            if target & 1 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1

        return moves + target - 1
            