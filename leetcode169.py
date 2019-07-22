from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        length = len(nums)
        
        for num in nums:
            d[num] += 1
            if d[num] * 2 > length:
                return num
