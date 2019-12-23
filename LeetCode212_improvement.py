# UTF-8
# LeetCode 212题 改进 单词搜索
# 日期 2019年12月23日 星期一

class Solution:
    
    def __init__(self):
        """
        初始化前缀树和记录表。
        """
        self.trie = dict()
        self.record = []

    def insert(self, word):
        """
        构建前缀树。
        """
        tempDict = self.trie

        for i in range(len(word)):
            if word[i] not in tempDict:
                tempDict[word[i]] = dict()
            tempDict = tempDict[word[i]]

        tempDict["True"] = 1

    def findWords(self, board, words):
        """
        寻找board是否存在单词。
        """
        # 行、列
        row = len(board)
        col = len(board[0])

        # 插入单词
        for word in words:
            self.insert(word)

        visit = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                self.DFS(board, i, j, "", row, col, visit, self.trie)

        return self.record

    def DFS(self, board, x, y, target, row, col, visit, tempDict):
        if "True" in tempDict and target not in self.record:
            self.record.append(target)

        if x < 0 or x >= row or y < 0 or y >= col or visit[x][y]:
            return
        
        visit[x][y] = True

        if board[x][y] in tempDict:
            self.DFS(board, x+1, y, target+board[x][y], row, col, visit,
            tempDict[board[x][y]])
            self.DFS(board, x-1, y, target+board[x][y], row, col, visit,
            tempDict[board[x][y]])
            self.DFS(board, x, y+1, target+board[x][y], row, col, visit,
            tempDict[board[x][y]])
            self.DFS(board, x, y-1, target+board[x][y], row, col, visit,
            tempDict[board[x][y]])

        visit[x][y] = False

# 测试
if __name__ == "__main__":
    s = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oate", "pea", "eat", "rain"]
    ans = s.findWords(board, words)
    print(s.trie)
    print(ans)
