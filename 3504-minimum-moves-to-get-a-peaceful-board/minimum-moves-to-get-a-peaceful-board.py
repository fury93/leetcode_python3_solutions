class Solution:
    def minMoves(self, rooks):
        min_moves = 0

        # Store the count of rooks in each row and column.
        row = [0] * len(rooks)
        col = [0] * len(rooks)
        for r in rooks:
            row[r[0]] += 1
            col[r[1]] += 1

        row_min_moves = 0
        col_min_moves = 0
        for i in range(len(rooks)):
            # Difference between the rooks count at row and column and one.
            row_min_moves += row[i] - 1
            col_min_moves += col[i] - 1

            # Moves required for row and column constraints.
            min_moves += abs(row_min_moves) + abs(col_min_moves)

        return min_moves