from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cjArr = [False for i in range(n)]
        cjArr[-1] = True
        for i in range(n-2, -1, -1):
            cj = False
            for j in range(i+1, i+1+nums[i]):
                if j < n:
                    cj = cj or cjArr[j]
                    if cj:
                        break
            cjArr[i] = cj
        return cjArr[0]