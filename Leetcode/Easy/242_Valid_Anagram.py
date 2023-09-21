class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            if t[i] != s[i] :
                return False
        return True
                
# Compare to best runtime solution: 
# thought: use Counter to count the number of each character in the string
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s)==Counter(t)