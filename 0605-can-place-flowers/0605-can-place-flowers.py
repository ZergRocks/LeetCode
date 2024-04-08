class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        
        if (
            length == 1
        ) and (
            flowerbed[0] == 0
        ) and (
            n < 2
        ):
            return True
        elif (
            length == 1
        ) and (
            flowerbed[0] == 0
        ) and (
            n > 2
        ):
            return False
            
        
        for i in range(length):
            if (
                i == 0
            ) and (
                flowerbed[i] == 0
            ) and (
                flowerbed[i + 1] == 0
            ):
                count += 1
                flowerbed[i] = 1
            elif (
                0 < i < length - 1
            ) and (
                flowerbed[i - 1] == 0
            ) and (
                flowerbed[i] == 0
            ) and (
                flowerbed[i + 1] == 0
            ):
                count += 1
                flowerbed[i] = 1
            elif (
                i == length - 1
            ) and (
                flowerbed[i] == 0
            ) and (
                flowerbed[i - 1] == 0
            ):
                count += 1
                flowerbed[i] = 1
        if n <= count:
            return True
        return False
                
                
                
                
                