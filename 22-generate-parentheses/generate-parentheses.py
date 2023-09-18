from functools import cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        openbs = n
        closebs = n
        @cache
        def combos(obs, cbs) -> List[str]:
            if obs > cbs or cbs == 0:
                return []
            if obs == 0 and cbs > 0:
                return [")" * cbs]
            csol = [ ")" + s for s in combos(obs, cbs-1)]
            osol = [ "(" + s for s in combos(obs-1, cbs)]
            return osol + csol
        return combos(n, n) 

