class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue_s = list(s)
        if len(s) < 1 :
            return True
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if queue_s[0] == t[i]:
                queue_s.pop(0)
            if not queue_s :
                return True
