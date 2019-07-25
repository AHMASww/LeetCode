import math
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        l = [0 for _ in range(32)]
        i = 0 
        while n >= 2:
            l[i] = n % 2
            n = n / 2
            i += 1
        l[i] = n
        
        l = l[::-1]
            
        for i in range(len(l)):
            ans += l[i] * math.pow(2, i)
            
        return int(ans)
