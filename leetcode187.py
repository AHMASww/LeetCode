'''
滑动窗口保存，计数
'''
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        d = defaultdict(int)
        ans = []
        
        for i in range(len(s) - 9):
            d[s[i:i+10]] += 1
            
        for key, value in d.items():
            if value > 1:
                ans.append(key)
                
        return ans
