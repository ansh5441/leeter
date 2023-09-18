class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        permuttt = []
        for perm in self.permute(nums[1:]):
            # add nums[0] in every position
            n = len(perm)
            for i in range(n+1):
                permuttt.append(
                    perm[:i] + [nums[0]] + perm[i:]
                )
        return permuttt

        