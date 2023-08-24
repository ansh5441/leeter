class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed.append(0)
        sz = len(flowerbed)-1
        prev = 0
        curr = flowerbed[0]
        for i in range(sz):
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n-= 1
                flowerbed[i] = 1
            if n <= 0:
                return True
            prev = flowerbed[i]
        return False
