class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        sorted_arr = sorted(arr)
        rank = 1
        rank_map = {sorted_arr[0]: rank}
        curr_num = sorted_arr[0]
        for a in sorted_arr:
            if a == curr_num:
                continue
            curr_num = a
            rank += 1
            rank_map[curr_num] = rank
        sol = []
        for a in arr:
            sol.append(rank_map[a])
        return sol