class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sa = [c for c in s]
        ta = [c for c in t]
        sa.sort()
        ta.sort()

        for i in range(len(s)):
            if sa[i] != ta[i]:
                return False
            
        return True