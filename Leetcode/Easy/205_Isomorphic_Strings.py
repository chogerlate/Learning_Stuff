import copy
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t={}
        for x in range(0,len(s)):
            if s[x] in map_s_to_t:
                if t[x]!=map_s_to_t[s[x]]:
                    return False
            else:
                if t[x] in map_s_to_t.values():
                    return False
            map_s_to_t[s[x]]=t[x]   
        return True
                
       