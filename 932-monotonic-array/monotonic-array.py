class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        i = 0
        while i < n-1 and nums[i] == nums[i+1]:
            i += 1
        if i == n-1:
            return True
        sign = nums[i+1] - nums[i]
        sign = sign // abs(sign)

        for j in range(i, n-1):
            if sign * (nums[j+1] - nums[j]) < 0:
                return False
        return True
        