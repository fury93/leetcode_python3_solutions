# TLE
class Solution1:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        total_array_sum = sum(arr)
        n = len(arr)

        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k
        taken = [False] * n
        
        def backtrack(count: int, curr_sum: int) -> bool:
            n = len(arr)

            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True

            # Current subset-sum exceeds target sum, no need to proceed further.
            if curr_sum > target_sum:
                return False

            # When current subset sum reaches target sum then one subset is made.
            # Increment count and reset current subset sum to 0.
            if curr_sum == target_sum:
                return backtrack(count + 1, 0)

            # Try not picked elements to make some combinations.
            for j in range(n):
                if not taken[j]:
                    # Include this element in current subset.
                    taken[j] = True

                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(count, curr_sum + arr[j]):
                        return True

                    # Backtrack step.
                    taken[j] = False

            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            return False

        return backtrack(0, 0)

class Solution2:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = [False] * n
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
      
            # We made k - 1 subsets with target_sum and the last subset must also have target_sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
                
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)
                
            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if not taken[j]:
                    # Include this element in current subset.
                    taken[j] = True
                    
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
        
                    # Backtrack step.
                    taken[j] = False
    
            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            return False
        
        return backtrack(0, 0, 0)

class Solution3:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        total_array_sum = sum(arr)
        
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = ['0'] * n
        
        memo = {}
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
            
            taken_str = ''.join(taken)
      
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
            
            # If we have already computed the current combination.
            if taken_str in memo:
                return memo[taken_str]
            
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            
            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if taken[j] == '0':
                    # Include this element in current subset.
                    taken[j] = '1'
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    # Backtrack step.
                    taken[j] = '0'
                    
            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            memo[taken_str] = False
            return memo[taken_str] 
        
        return backtrack(0, 0, 0)

class Solution4:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        mask = 0
        
        memo = {}
        
        def backtrack(index, count, curr_sum):
            nonlocal mask
            n = len(arr)
            
            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            
            # No need to proceed further.
            if curr_sum > target_sum:
                return False
            
            # If we have already computed the current combination.
            if mask in memo:
                return memo[mask]
            
            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[mask] = backtrack(0, count + 1, 0)
                return memo[mask]

            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if ((mask >> j) & 1) == 0:
                    # Include this element in current subset.
                    mask = (mask | (1 << j))

                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    # Backtrack step.
                    mask = (mask ^ (1 << j))

            # We were not able to make a valid combination after picking 
            # each element from the array, hence we can't make k subsets.
            memo[mask] = False
            return memo[mask] 

        return backtrack(0, 0, 0)

class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        total_array_sum = sum(arr)
        n = len(arr)
        
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        subsetSum = [-1] * (1 << n)
        # Initially only one state is valid, i.e don't pick anything
        subsetSum[0] = 0

        for mask in range(1 << n):
            # If the current state has not been reached earlier.
            if subsetSum[mask] == -1: 
                continue

            for i in range(n):
                # If the number arr[i] was not picked earlier, and arr[i] + subsetSum[mask]
                # is not greater than the targetSum then add arr[i] to the subset
                # sum at subsetSum[mask] and store the result at subsetSum[mask | (1 << i)].
                if (mask & (1 << i)) == 0 and subsetSum[mask] + arr[i] <= target_sum: 
                    subsetSum[mask | (1 << i)] = (subsetSum[mask] + arr[i]) % target_sum
                
            if subsetSum[-1] == 0: 
                return True
        
        return subsetSum[-1] == 0