from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        prev = 2
        curr = 3
        for i in range(3, n):
            curr = prev + curr
            prev = curr - prev
        return curr