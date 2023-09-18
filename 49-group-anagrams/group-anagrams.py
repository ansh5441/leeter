class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sam = collections.defaultdict(list)
        for s in strs:
            star = [c for c in s]
            star.sort()
            sam[tuple(star)].append(s)
        return list(sam.values())
        
        