class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = [*str((int(a) + int(b)))]
        for i in range(len(result)-1,-1,-1):
            if i == 0 and int(result[i]) > 1:
                result[i] =  '0' if int(result[i]) == 2 else  '1'
                result.insert(0,'1')
                break
            if int(result[i]) > 2 :
                result[i] = '1' 
                result[i-1] = str(int(result[i-1]) + 1)
            elif int(result[i]) > 1 :
                result[i] = '0' 
                result[i-1] = str(int(result[i-1]) + 1)
        print(result)
        return "".join(result)