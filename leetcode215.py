'''
快排思想，平均O(n)，最坏O(n^2)
'''
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:      
        while True:
            index = random.randint(0, len(nums)-1)
            left, right = self.quickSort(nums, index)
            
            if len(right) == k-1:
                return nums[index]
            elif len(right) < k-1:
                nums = left
                k = k - len(right) - 1
            else:
                nums = right
                
    
    def quickSort(self, nums, index):
        left, right = [], []
        for i in range(len(nums)):
            if i == index:
                continue
            elif nums[i] <= nums[index]:
                left.append(nums[i])
            elif nums[i] > nums[index]:
                right.append(nums[i])
        
        return left, right
