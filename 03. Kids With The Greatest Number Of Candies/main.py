from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n
        
        for index, candy in enumerate(candies):
            if candy + extraCandies >= max(candies):
                result[index] = True
        return result