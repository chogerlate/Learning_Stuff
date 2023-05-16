class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        str_num = str(abs(x))
        print(len(str_num))
        i = 0 
        j = len(str_num) -1

        if len(str_num) == 0 :
            return True
        while i <= j :
            if str_num[i] != str_num[j]:
                print("here")
                return False
            i += 1
            j -= 1
        return True