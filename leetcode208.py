'''
构造27叉树，0-25位孩子节点，26位是否独立单词节点
'''
class Node:
    def __init__(self):
        self.next = [None for _ in range(27)]

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """ 
        head = self.root
        while len(word):
            if head.next[ord(word[0]) - 97] == None:
                newNode = Node()
                head.next[ord(word[0]) - 97] = newNode
            head = head.next[ord(word[0]) - 97] 
            word = word[1:]
        head.next[26] = True 
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head = self.root
        while len(word): 
            if head.next[ord(word[0]) - 97] != None:
                head = head.next[ord(word[0]) - 97]
                word = word[1:]
            else:
                return False
            
        if not head.next[26]:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        while len(prefix):
            if head.next[ord(prefix[0]) - 97]:
                head = head.next[ord(prefix[0]) - 97]
                prefix = prefix[1:]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
