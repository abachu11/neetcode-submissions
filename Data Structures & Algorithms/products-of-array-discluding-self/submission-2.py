from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        l = len(nums)
        result = []

        for i in nums:
            if i == 0:
                zeros += 1
                if zeros == 2:
                    return [0] * l
                continue
            prod *= i  # Multiply non-zero numbers
            
        if zeros == 0:
            # When no zeros, divide product by each element
            for i in nums:
                result.append(prod // i)
        else:
            # When exactly one zero
            for i in nums:
                if i == 0:
                    result.append(prod)
                else:
                    result.append(0)
        
        return result
