class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ds = []
        for index, row in enumerate(mat):
            ds.append((sum(row), index))
        ds = sorted(ds, key=lambda x: (1000 * x[0] + x[1]))
        sol = []
        for i in range(k):
            sol.append(ds[i][1])
        return sol