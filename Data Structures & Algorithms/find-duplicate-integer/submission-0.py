from collections import defaultdict 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums_dict = {}
        curr = nums
        
        for num in nums:
            if num in nums_dict:
                return num
            else:
                nums_dict[num] = 0

    
        

        