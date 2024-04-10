from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums

s = Solution()
print(s.moveZeroes([1, 0, 2, 3, 0, 20]))