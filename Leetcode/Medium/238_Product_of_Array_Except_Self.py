class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """return list that each element is result from product of all elements except self in nums

        Args:
            nums (List[int]): input list of numbers

        Returns:
            List[int]: result 
        """
        # create list and set the left most element to 1
        answer = []
        answer.append(1)

        # iterate from left accumulate product of all elements except self
        for i in range(1,len(nums)):
            answer.append( answer[i-1] * nums[i-1] )

        # iterate from right accumulate product of all elements except self
        right = 1 # create variable to store product of all elements from right 
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right # multiply product of all elements from left and right
            right *= nums[i] # accumulate product of all elements from right

        return answer

