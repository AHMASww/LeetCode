#UTF-8
#LeetCode 208题
#实现Trie(前缀树)
#日期：2019年12月19日 星期四

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictory = dict()

    def insert(self, word):
        """
        Insert a word into the trie.
        """
        tempDict = self.dictory
        for i in range(len(word)):
            if word[i] not in tempDict:
                tempDict[word[i]] = dict()
            tempDict = tempDict[word[i]]

        tempDict["True"] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
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

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prifix.
        """
        tempDict = self.dictory
        for i in range(len(prefix)):
            if prefix[i] not in tempDict:
                return False
            else:
                tempDict = tempDict[prefix[i]]

        return True

#测试
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
