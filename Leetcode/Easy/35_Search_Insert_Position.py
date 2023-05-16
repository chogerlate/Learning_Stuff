class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
            if nums[len(nums)-1-i] == target:
                return len(nums)-1-i
        return len(nums)