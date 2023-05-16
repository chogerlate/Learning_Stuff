class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ck = []
        pop_count = 0 
        for item in nums:
            if item in ck:
                continue  
            else :
                ck.append(item)
                nums[pop_count] = item
                pop_count += 1 
        # print(nums)
        return pop_count