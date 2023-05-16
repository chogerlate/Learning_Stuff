class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = 0, len(s)-1
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha() :
                end = i
                print(f'got it ending {end}')
                for j in range(i,-1,-1):
                    if s[j].isalpha():
                        start = j
                        print(f'got it starting {start}')
                    else :
                        break
                break
        return end - start + 1