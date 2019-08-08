'''
BFS、贪心解法
'''
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        # 邻接表
        table = [set() for _ in range(numCourses)]
        # 每个点的入度
        dic = {key : 0 for key in range(numCourses)}
        queue = deque()
        ans = []
        
        for item in prerequisites:
            dic[item[0]] += 1
            table[item[1]].add(item[0])
        # 寻找入度为0的点   
        for key, value in dic.items():
            if value == 0:
                queue.append(key)
                
        while queue:
            temp = queue.popleft()
            ans.append(temp)
            # 将以popleft()的点为条件的点的入度减去1
            for next in table[temp]:
                dic[next] -= 1
                # 如果入度为0，则放入queue队列中
                if dic[next] == 0:
                    queue.append(next)
        # 防止存在环
        if len(ans) == numCourses:
            return ans
        
        return []
