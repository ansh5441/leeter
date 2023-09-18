class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combsum(targ):
            if targ == 0:
                return [[]]
            if targ < 0:
                return []
            nonlocal candidates
            sol = set()
            for c in candidates:
                subsol = combsum(targ - c)
                for sl in subsol:
                    combo = [c] + sl
                    combo.sort()
                    sol.add( tuple(combo) )
            return [ list(k) for k in sol]

        return combsum(target)

