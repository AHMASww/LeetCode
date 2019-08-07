class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        min_length = float("inf")
        start, end = 0, 0
        
        temp_sum = nums[end] 
        while end < len(nums):
            if temp_sum < s:
                end += 1
                if end < len(nums):
                    temp_sum += nums[end]
            else:
                min_length = min(min_length, end-start+1)
                temp_sum -= nums[start]
                start += 1
        
        if min_length == float("inf"):
            return 0
        return min_length
