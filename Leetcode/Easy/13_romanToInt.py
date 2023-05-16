class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0 #start
        data = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        save_num = 0 
        for a,b in zip(s,s[1:]):
            if data[a] < data[b]:
                result -= data[a]
            else :
                result += data[a]
        return result + data[s[-1]]