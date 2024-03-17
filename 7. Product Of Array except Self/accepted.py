from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
