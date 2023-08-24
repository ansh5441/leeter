class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while j > i:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > 0 and not s[j].isalnum():
                j -= 1
            if j <= i:
                return True
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True