class Solution:
    def finalString(self, s: str) -> str:
        new_arr = []
        n = len(s)
        j = 0
        while j < n:
            if j < n-1 and s[j] == 'i' and s[j+1] == "i":
                j+=1
            else:
                if s[j] == "i":
                    new_arr.reverse()
                else:
                    new_arr.append(s[j])
            j += 1
        return "".join(new_arr)
            