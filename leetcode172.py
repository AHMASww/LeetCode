class Solution:
    def trailingZeroes(self, n: int) -> int:
        five_num = n // 5
        extra_five_num = five_num
        while extra_five_num != 0:
            extra_five_num = extra_five_num // 5 
            five_num += extra_five_num
        
        return five_num
