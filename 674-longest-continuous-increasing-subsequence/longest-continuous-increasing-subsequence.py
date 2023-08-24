class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numInc = 1
        currMax = nums[0]
        currIndex = 1
        while currIndex < len(nums) and nums[currIndex] > currMax:
            currMax = nums[currIndex]
            currIndex += 1
            numInc += 1
        return max(numInc, self.findLengthOfLCIS(nums[currIndex:]))

