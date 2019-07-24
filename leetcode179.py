'''
比较 (string1 + string2) 和 (string2 + string1) 大小即可
'''
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def tcmp(x, y):
            if x + y >= y + x:
                return -1 
            else:
                return 1 
        
        nums = list(map(str, nums))
        nums = sorted(nums, key = functools.cmp_to_key(tcmp))
        
        for i in range(len(nums)):
            if nums[i] != "0":
                break
        nums = nums[i:]
        
        return "".join(nums)
