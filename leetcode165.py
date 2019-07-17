class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = list(map(int, version1.split(".")))
        v2_list = list(map(int, version2.split(".")))
        
        v1_list = v1_list[:self.trueLength(v1_list)]
        v2_list = v2_list[:self.trueLength(v2_list)]

        if v1_list > v2_list:
            return 1
        elif v1_list < v2_list:
            return -1
        else: return 0
                       
        return 0
    
    def trueLength(self, version):
        length = len(version)
        for i in range(len(version)-1, -1, -1):
            if version[i] == 0:
                length -= 1
            else:
                return length
            
        return length
