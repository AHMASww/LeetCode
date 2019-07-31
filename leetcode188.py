'''
解题评论中的方法 “一个通用方法团灭6道股票问题”
通过枚举状态来遍历所有情况
当k > len(prices)//2时，意味着k已经没有限制了，可以转为贪心算法：
    假设第一天买，第二天卖，以此循环，最多也是len(prices)//2的数量
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0
        if k > len(prices) // 2:
            ans = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    ans += prices[i] - prices[i-1]
            return ans
        else:
            P = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices)+1)]
            # 初始化开始情况
            for i in range(k+1):
                P[0][i][0], P[0][i][1] = 0, float("-inf")
            for i in range(len(prices)+1):
                P[i][0][0], P[i][0][1] = 0, float("-inf")

            for d in range(1, len(prices)+1):
                for t in range(1, k+1):
                    P[d][t][0] = max(P[d-1][t][0], P[d-1][t][1]+prices[d-1])
                    P[d][t][1] = max(P[d-1][t][1], P[d-1][t-1][0]-prices[d-1])

            return P[len(prices)][k][0]
