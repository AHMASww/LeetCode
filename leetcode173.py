# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
# LDR方法不符合空间要求
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.TreeNode_list = []
        self.LDR(root)
     
    def LDR(self, root):
        if not root: return
        self.LDR(root.left)
        self.TreeNode_list.append(root.val)
        self.LDR(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.TreeNode_list[0]
        self.TreeNode_list = self.TreeNode_list[1:]
        return ans

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.TreeNode_list) != 0:
            return True
        else:
            return False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur_node = self.stack.pop()
        ans = cur_node.val
        cur_node = cur_node.right
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left
        return ans

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack: return True
        else: return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
