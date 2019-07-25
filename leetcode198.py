class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
        
        money = [0 for _ in range(len(nums))]
        money[0], money[1], money[2] = nums[0], max(nums[0], nums[1]), nums[0]+nums[2]
        
        for i in range(3, len(nums)):
            money[i] = nums[i] + max(money[i-2], money[i-3])
            
        print(money)
        
        return max(money[-2], money[-1])
