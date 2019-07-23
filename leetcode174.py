'''
反向动态规划，即从终点走到起点。若从起点出发，每格包含两种衡量值：
当前所需健康值和当前健康值，则这格确定则需要下一行来决定。
反向动态规划时，若遇到该格的当前健康值大于0，则应将健康值设为0，
因为当前剩余的健康值无法和前期所受到上海抵消。
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, column = len(dungeon), len(dungeon[0])
        
        health = [[0 for _ in range(column)] for _ in range(row)]
        health[row-1][column-1] = dungeon[row-1][column-1]
        
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                if i+1 < row and j+1 < column:
                    health[i][j] = dungeon[i][j] + max(health[i+1][j], health[i][j+1]) 
                elif i+1 < row:
                    health[i][j] = dungeon[i][j] + health[i+1][j]
                elif j+1 < column:
                    health[i][j] = dungeon[i][j] + health[i][j+1]
                if health[i][j] > 0:
                    health[i][j] = 0
        return abs(health[0][0]) + 1
