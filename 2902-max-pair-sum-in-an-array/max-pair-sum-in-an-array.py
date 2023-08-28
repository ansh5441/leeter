from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_digit_map = defaultdict(list)
        for num in nums:
            digits = [ int(k) for k in str(num) ]
            nums_digit_map[max(digits)].append(num)
        max_sum = -1
        for k in nums_digit_map.keys():
            if len(nums_digit_map[k]) < 2:
                continue
            else:
                vals = [x for x in nums_digit_map[k]]
                vals.sort(reverse=True)
                max_sum = max(max_sum, sum(vals[:2]))
        return max_sum

