import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """return top k frequent elements in nums

        Args:
            nums (List[int]): input sequnece of numbers
            k (int): top k frequent elements

        Returns:
            List[int]: list of top k frequnet elements
        """
        # using collection.Counter to create dictionary of frequnecy of each element
        # then sort the dictionary by value in descending order
        freq_nums = dict(sorted(collections.Counter(nums).items(),key=lambda x:x[1],reverse=True))
        
        # return top k frequent elements
        return list(freq_nums.keys())[:k]

    