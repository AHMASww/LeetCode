'''
DFS回溯，注意步长为4
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        ans = []
        length = 4
        def DFS(start, tmp, ans, s, length):
            if start == len(s) and length == 0:
                ans.append(tmp[:-1])
                return
            if length < 0 or start >= len(s):
                return
            
            if s[start] == "0":
                DFS(start+1, tmp+"0.", ans, s, length-1)
            else:
                for i in range(1, 4):
                    if int(s[start:start+i]) >= 0 and int(s[start:start+i]) <= 255:
                        DFS(start+i, tmp+s[start:start+i]+".", ans, s, length-1)
                        
        DFS(0, "", ans, s, length)
        
        return ans
