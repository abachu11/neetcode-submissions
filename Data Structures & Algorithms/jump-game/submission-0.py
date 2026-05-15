class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums)-1

        curr_index = last_index-1
        while curr_index > -1:
            if nums[curr_index] > last_index-curr_index:
                last_index = curr_index
                curr_index = curr_index-1
            curr_index = curr_index - 1
        
        return last_index == 0