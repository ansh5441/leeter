from functools import cache
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        @cache
        def subs(k):
            if k == n:
                return [()]
            sols = subs(k+1)
            return [(nums[k],)] + [(nums[k],) + s for s in sols if len(s) > 0 and nums[k] <= s[0]] + sols
        return [ list(k) for k in set(subs(0)) if len(k) > 1]