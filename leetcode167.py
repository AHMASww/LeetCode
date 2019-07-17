class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x, y = 0, len(numbers)-1
        while x < y:
            s = numbers[x] + numbers[y]
            if s == target:
                return [x+1, y+1]
            elif s > target:
                y -= 1
            else:
                x += 1
        
        return []
