'''
DFS解法
'''
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1 or len(prerequisites) == 0:
            return True
        
        table = [set() for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        dic = {key : 0 for key in range(numCourses)}
        queue = deque()
        for item in prerequisites:
            table[item[1]].add(item[0])
            dic[item[0]] += 1
        # 从入度为0的点出发
        for key, value in dic.items():
            if value == 0:
                queue.append(key)
        # 如果没有入度为0的点，则不可能为拓扑排序
        if not queue:
            return False
        
        while queue:
            if not self.DFS(table, visit, queue.popleft()):
                return False
        # 如果还有没有遍历的点，则一定为环
        for v in visit:
            if v == 0:
                return False

        return True
    
    def DFS(self, table, visit, x):
        # 上一次循环已经遍历过的点
        if visit[x] == 1:
            return True
        # 该次循环遍历过的点，如果同一次遍历中遇到两侧同样的点，则为环
        if visit[x] == 2:
            return False
        # 将该次遍历过的点设置为2
        visit[x] = 2
        for next_node in table[x]:
            if not self.DFS(table, visit, next_node):
                return False
        # 将结束遍历过的点设置为1
        visit[x] = 1
        return True

'''
BFS解法，贪心解法
'''
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1 or len(prerequisites) == 0:
            return True
        
        table = [set() for _ in range(numCourses)]
        dic = {key : 0 for key in range(numCourses)} 
        num = 0
        queue = deque()
       
        for item in prerequisites:
            table[item[1]].add(item[0])
            dic[item[0]] += 1
        # 从入度为0的点出发
        for key, value in dic.items():
                if value == 0:
                    queue.append(key)
                    dic[key] = -1    
                    
        while num < numCourses:
            # 如果没有入度为0的点，剩余点一定为环
            if len(queue) == 0:
                return False
            
            temp = queue.popleft()
            num += 1
            # 将该点及其边删去，重新寻找新的入度为0的点
            for x in table[temp]:
                if dic[x] == 1:
                    dic[x] = -1
                    queue.append(x)
                else: dic[x] -= 1
                    
        return True
