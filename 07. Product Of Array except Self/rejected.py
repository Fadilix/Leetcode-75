from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def product_list_except_t(array, t):
            product = 1
            for i in range(len(array)):
                if array[i] != t:
                    product *= array[i]
            return product

        result = []
        for i in range(len(nums)):
            prod = product_list_except_t(nums, nums[i])
            result.append(prod if prod != 1 else 0)
        return result
