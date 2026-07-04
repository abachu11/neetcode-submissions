class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictmap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in dictmap:
                return [dictmap[diff], index]
            dictmap[num] = index
