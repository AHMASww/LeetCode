# UTF-8
# LeetCode 212题 单词搜索
# 日期 2019年12月19日 星期四

class Trie:
    
    def __init__(self):
        """
        初始化前缀树。
        """
        self.dictory = dict()

    def insert(self, word):
        """
        插入单词。
        """
        tempDict = self.dictory
    
        for i in range(len(word)):
            if word[i] not in tempDict:
                tempDict[word[i]] = dict()

            tempDict = tempDict[word[i]]

        tempDict["True"] = 1

    def search(self, word):
        """
        寻找单词。
        """
        tempDict = self.dictory

        for i in range(len(word)):
            if word[i] not in tempDict:
                return False
            tempDict = tempDict[word[i]]

        if "True" in tempDict:
            return True
        else:
            return False

    def startWith(self, prefix):
        """
        寻找前缀。
        """
        tempDict = self.dictory

        for i in range(len(prefix)):
            if prefix[i] not in tempDict:
                return False
            tempDict = tempDict[prefix[i]]

        return True


class Solution:

    def __init__(self):
        """
        初始化前缀树和记录表。
        """
        self.trie = Trie()
        self.record = []

    def findWords(self, board, words):
        """
        寻找board是否存在单词。
        """
        # 构建前缀树
        for word in words:
            self.trie.insert(word)

        # 行、列
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                visit = [[False for _ in range(col)] for _ in range(row)]
                self.DFS(board, i, j, "", row, col, visit)

        return self.record

    def DFS(self, board, x, y, target, row, col, visit):
        if x < 0 or x >= row or y < 0 or y >= col or visit[x][y]:
            return
        
        visit[x][y] = True
        target += board[x][y]
        if self.trie.search(target) and target not in self.record:
            self.record.append(target)

        if self.trie.startWith(target):
            self.DFS(board, x+1, y, target, row, col, visit)
            self.DFS(board, x-1, y, target, row, col, visit)
            self.DFS(board, x, y+1, target, row, col, visit)
            self.DFS(board, x, y-1, target, row, col, visit)

        visit[x][y] = False

        return


# 测试
if __name__ == "__main__":
    s = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    #board = [["a","b"],["c","d"]]
    #words=["cdba"]
    #board = [["a","b"],["a","a"]]
    #words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

    ans = s.findWords(board, words)
    print(ans)
