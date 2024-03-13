class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea, heights = 0, [0] * (len(matrix[0]) + 1)
        
        for row in matrix:
            for i, v in enumerate(row):
                heights[i] = heights[i] + 1 if v == '1' else 0
            stack = [-1]
            for i, v in enumerate(heights):
                while stack and heights[stack[-1]] > v:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        
        return maxArea
    
    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        maxArea, heights = 0, [0] * (len(matrix[0]) + 1)
        
        for row in matrix:
            for i, v in enumerate(row):
                heights[i] = heights[i] + 1 if v == '1' else 0
            stack = [-1]
            for i, v in enumerate(heights):
                while stack and heights[stack[-1]] > v:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        
        return maxArea

    def is_proper_rect(self, matrix, left_top, right_bottom):
        for x in range(left_top[0], right_bottom[0] + 1):
            for y in range(left_top[1], right_bottom[1] + 1):
                if matrix[y][x] == "0":
                    return False
        return True

    def extend_rect(self, matrix, left_top, right_bottom):
        if not self.is_proper_rect(matrix, left_top, right_bottom):
            return 0

        matrix_w = len(matrix[0])
        matrix_h = len(matrix)

        w = right_bottom[0] - left_top[0] + 1
        h = right_bottom[1] - left_top[1] + 1
        rect_square = w * h

        # top
        if left_top[1] - 1 > 0:
            top = self.extend_rect(matrix, (left_top[0], left_top[1] - 1), right_bottom)
            rect_square = max(top, rect_square)

        # right
        if right_bottom[0] + 1 < matrix_w:
            right = self.extend_rect(matrix, left_top, (right_bottom[0] + 1, right_bottom[1]))
            rect_square = max(right, rect_square)

        # bottom
        if right_bottom[1] + 1 < matrix_h:
            bottom = self.extend_rect(matrix, left_top, (right_bottom[0], right_bottom[1] + 1))
            rect_square = max(bottom, rect_square)

        # left
        if left_top[0] - 1 > 0:
            rect_square = max(self.extend_rect(matrix, (left_top[0] - 1, left_top[1]), right_bottom), rect_square)

        return rect_square


    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        max_rect = 0
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if cell == "0":
                    continue
                max_rect = max(self.extend_rect(matrix, (x, y), (x, y)), max_rect)

        return max_rect

