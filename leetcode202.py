'''
对于不是快乐数的值，最终都会陷入循环
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        self.value = []
        while n != 1:
            if n in self.value:
                return False
            self.value.append(n)
            n = self.cal(n)
            
        return True
        
    def cal(self, n):
        temp = [int(i) for i in str(n)]
        ans = 0
        for i in temp:
            ans += i*i
            
        return an
