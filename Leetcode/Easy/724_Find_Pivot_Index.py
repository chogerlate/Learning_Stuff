class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivotIndexList =[]
        leftToRight = list(nums) 
        rightToLeft = list(nums)
        answer = -1 

        for i in range(1,len(nums)):
            leftToRight[i] = leftToRight[i-1] + nums[i]
        for i in range(len(nums)-2,-1,-1):
            rightToLeft[i] = rightToLeft[i+1] + nums[i]
        
        for i in range(len(nums)):
            if leftToRight[i] == rightToLeft[i]:
                answer =  i
                break 
                print(answer)
        
        # if answer == 0 or answer == len(nums)-1 :
        #     answer = 0
        

        print(leftToRight,rightToLeft)

        return answer