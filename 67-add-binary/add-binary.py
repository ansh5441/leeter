class Solution:
    def addBinary(self, a: str, b: str) -> str:
      smaller = a if len(a) < len(b) else b
      larger = b if len(a) < len(b) else a
      n = len(larger)
      m = len(smaller)
      carry = 0
      res = ""
      for i in range(n-1,-1,-1):
        total = 0
        small_index = i + m - n
        if small_index >= 0:
          total += int(smaller[small_index])
        total += carry + int(larger[i])
        
        res = str(total % 2) + res
        carry = int(total / 2)
      if carry > 0:
        res = str(carry) + res
      return res


      