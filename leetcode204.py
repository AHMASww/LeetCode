class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        else:
            ans = [1] * n
            ans[0], ans[1] = 0, 0
            for i in range(2, int(math.sqrt(n)) + 1):
                if ans[i] == 1:
                    ans[i*i:n:i] = [0] * len(ans[i*i:n:i])
                    
        return sum(ans)
