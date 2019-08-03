class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        
        if len(s) != len(t):
            return False
        
        dic1 = dict()
        dic2 = dict()
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = t[i]
            elif dic1[s[i]] != t[i]:
                return False
            
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            elif dic2[t[i]] != s[i]:
                return False
                
        return True
