class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        last = 0
        curr = 1
        for i in range(1, n):
            last, curr = curr, last + curr
        return curr
        