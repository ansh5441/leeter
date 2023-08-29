class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cust_arr = [ 0 if k == "N" else 1 for k in customers ]
        min_penalty = sum(cust_arr)
        close_at = 0
        penalty = min_penalty
        for i, c in enumerate(cust_arr):
            if c == 1:
                penalty -= 1
                if penalty < min_penalty:
                    close_at = i + 1
                    min_penalty = penalty
            else:
                penalty += 1
        return close_at