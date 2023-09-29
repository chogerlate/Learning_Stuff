class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """find the longest consecutive sequence in an unsorted array of integers

        Args:
            nums (List[int]): unsorted array of integers

        Returns:
            int: length of the longest consecutive sequence
        """
        seq = set(nums) # unique elements
        cur_len = 0 # current length
        max_len = 0 # max length 
        
        for num in nums :
            # if num-1 is not in the set, then num is the start of a sequence
            if not(num-1 in seq) :
                # find the length of the sequence
                cur_num = num
                cur_len = 1
                while cur_num+1 in seq :
                    # if cur_num+1 is in the set, then the sequence continues
                    cur_len +=1 
                    cur_num = cur_num + 1
                    
                    # optimization: remove the element from the set to avoid duplicate counting
                    seq.discard(cur_num-1) # hasten the search
                    
                max_len = max(cur_len, max_len) # update max_len
        return max_len
    