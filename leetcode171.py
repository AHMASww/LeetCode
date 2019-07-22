import math
class Solution:
    def titleToNumber(self, s: str) -> int:
        label = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        ans = 0 
        s = s[::-1]
        for i in range(len(s)):
            ans += (label.index(s[i])+1) * math.pow(26, i)
                
        return int(ans)
