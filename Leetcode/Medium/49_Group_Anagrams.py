class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        [d[''.join(sorted(i))].append(i) for i in strs]
        return d.values()