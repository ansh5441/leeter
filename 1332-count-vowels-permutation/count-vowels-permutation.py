from functools import cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def count_per(n, last):
            if n == 1:
                return 1
            n = n - 1
            if last == "a":
                return count_per(n, "e")
            elif last == "e":
                return count_per(n, "a") + count_per(n, "i")
            elif last == "i":
                return sum([ count_per(n, k) for k in ["a", "e", "o", "u"] ])
            elif last == "o":
                return count_per(n, "i") + count_per(n, "u")
            elif last == "u":
                return count_per(n, "a")        
        return sum([ count_per(n, k) for k in ['a', 'e', 'i', 'o', 'u'] ]) % (10**9 + 7)