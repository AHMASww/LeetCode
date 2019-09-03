class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        row, col = len(matrix) ,len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        max_value = 0
        # 初始化第0行和第0列
        for i in range(col):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                max_value = max(max_value, dp[0][i])
        for i in range(row):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                max_value = max(max_value, dp[i][0])
                
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_value = max(dp[i][j], max_value)
        
        return max_value**2
