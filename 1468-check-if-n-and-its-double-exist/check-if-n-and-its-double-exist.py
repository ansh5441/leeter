class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles_map = {}
        for ind, a in enumerate(arr):
            doubles_map[a*2] = ind
        for k, a in enumerate(arr):
            j = doubles_map.get(a)
            if j is not None and j != k:
                return True
        return False