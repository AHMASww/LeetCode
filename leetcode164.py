'''
基于桶排序
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = list(set(nums))
        length = len(nums)
        if length < 2:
            return 0
        elif length == 2:
            return abs(nums[0] - nums[1])
        
        ans = float("-inf")
        
        max_num, min_num = max(nums), min(nums)
        bucket_num = (max_num - min_num) // ((max_num - min_num) // (length - 1)) + 1
        buckets = [[float("inf"), float("-inf")] for _ in range(bucket_num)]
        
        for num in nums:
            index = (num - min_num) // ((max_num - min_num) // (length - 1))
            if num < buckets[index][0]:
                buckets[index][0] = num
            if num > buckets[index][1]:
                buckets[index][1] = num
        
        x, y = 0, 1
        while y < bucket_num:
            if buckets[x][1] == float("-inf"):
                x += 1
                if x == y:
                    y += 1
            elif buckets[y][0] == float("inf"):
                y += 1
            else:
                if buckets[y][0] - buckets[x][1] > ans:
                    ans = buckets[y][0] - buckets[x][1]
                x += 1
                y += 1
                
        return ans
