class Solution:
    def tourOfKnight(self, m, n, r, c):
        # Precompute possible knight moves
        moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        def _is_valid_move(to_row, to_col):
            return (
                0 <= to_row < m
                and 0 <= to_col < n
                and chessboard[to_row][to_col] == 0
            )

        def _solve_knights_tour(current_row, current_col, move_count):
            # Base case: if all cells have been visited, we've found a solution
            if move_count == m * n:
                return True

            # Try all possible knight moves
            for move_r, move_c in moves:
                new_row, new_col = current_row + move_r, current_col + move_c
                # Check if the move is valid
                if _is_valid_move(new_row, new_col):
                    chessboard[new_row][new_col] = move_count

                    # Recursively try to solve from this new position
                    if _solve_knights_tour(new_row, new_col, move_count + 1):
                        return True

                    # If the move doesn't lead to a solution, backtrack
                    chessboard[new_row][new_col] = 0

            # If no solution is found from the current position
            return False

        chessboard = [[0] * n for _ in range(m)]

        chessboard[r][c] = -1

        # Start the recursive solving process
        _solve_knights_tour(r, c, 1)

        chessboard[r][c] = 0

        return chessboard