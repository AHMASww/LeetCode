# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans = [[root, 0]]
        final_ans = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            cur_node = queue.popleft()
            if cur_node[0].left:
                queue.append([cur_node[0].left, cur_node[1] + 1])
                ans.append([cur_node[0].left, cur_node[1] + 1])
            if cur_node[0].right:
                queue.append([cur_node[0].right, cur_node[1] + 1])
                ans.append([cur_node[0].right, cur_node[1] + 1])
        for i in range(len(ans)-1):
            if ans[i][1] != ans[i+1][1]:
                final_ans.append(ans[i][0].val)
        final_ans.append(ans[-1][0].val)
            
        return final_ans
