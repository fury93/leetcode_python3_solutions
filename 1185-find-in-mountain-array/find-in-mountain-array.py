class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        peak_index = low

        # 2. Search in the strictly increasing part of the array
        low = 0
        high = peak_index
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index    
        # Check if the target is present in the strictly increasing part
        if mountain_arr.get(low) == target:
            return low
        
        # 3. Otherwise, search in the strictly decreasing part
        low = peak_index + 1
        high = length - 1
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        # Check if the target is present in the strictly decreasing part
        if mountain_arr.get(low) == target:
            return low
        
        # Target is not present in the mountain array
        return -1


class Solution2:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index) 
            next = mountain_arr.get(test_index + 1)
            
            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        
        peak_index = low

        # 2. Search in the strictly increasing part of the array
        # If found, will be returned in the loop itself.
        low = 0
        high = peak_index
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        # 3. Search in the strictly decreasing part of the array
        # If found, will be returned in the loop itself.
        low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        # Target is not present in the mountain array
        return -1    