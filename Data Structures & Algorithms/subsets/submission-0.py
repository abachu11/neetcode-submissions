from copy import deepcopy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb = [[]]
        n = len(nums)

        def btrack_subsets(comb,new_nums):
            new_copy  = deepcopy(comb)
            if new_nums:
                for i in range(len(new_copy)):
                    new_copy[i].append(new_nums[0])
            comb += new_copy
            if new_nums[1::]:
                comb = btrack_subsets(comb,new_nums[1:])
            return comb
        return  btrack_subsets(comb,nums)
