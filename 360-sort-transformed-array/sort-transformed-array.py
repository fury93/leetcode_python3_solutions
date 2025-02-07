# Approach 2: Two Pointers
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(x):
            # Return the transformed result for element 'x'
            return (a * x * x) + (b * x) + c

        answer = []
        left, right = 0, len(nums) - 1
        
        if a < 0:
            # When 'downward parabola' we will put the edge element (smaller elements) first.
            while left <= right:
                left_transformed_val = transform(nums[left])
                right_transformed_val = transform(nums[right])
                if left_transformed_val < right_transformed_val:
                    answer.append(left_transformed_val)
                    left += 1
                else:
                    answer.append(right_transformed_val)
                    right -= 1
        else:
            while left <= right:
                # When 'upward parabola' or a 'straight line' 
                # we will put the edge element (bigger elements) first.
                left_transformed_val = transform(nums[left])
                right_transformed_val = transform(nums[right])
                if left_transformed_val > right_transformed_val:
                    answer.append(left_transformed_val)
                    left += 1
                else:
                    answer.append(right_transformed_val)
                    right -= 1
            # Reverse the decreasing 'answer' array.
            answer.reverse()
        return answer

# Approach 3: Non-Comparison Based Sorting
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        answer = [0] * len(nums)
        for i, num in enumerate(nums):
            # Push transformed value in 'answer' array.
            answer[i] = (a * num * num) + (b * num) + c

        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for num in answer:
            max_element = max(abs(num), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element /= 10

        place_value = 1
        def sort():
            map_digits = [[] for i in range(10)]
            for num in answer:
                digit = abs(num) / place_value
                digit = int(digit % 10)
                map_digits[digit].append(num)

            # Overwrite 'answer' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for num in map_digits[digit]:
                    answer[index] = num
                    index += 1

        # Radix sort, least significant digit place to most significant.      
        for _ in range(max_digits):
            sort()
            place_value *= 10

        # Seperate out negatives and reverse them. 
        positives = [num for num in answer if num >= 0]
        negatives = [num for num in answer if num < 0]
        negatives.reverse()

        # Final 'answer' will be 'negative' elements, then 'positive' elements.
        answer = negatives + positives
        return answer
