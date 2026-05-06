class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        
        max_amount = [0]*n
        max_amount[0] = nums[0]
        max_amount[1] = max(nums[0],nums[1])
        max_amount[2] = max((nums[0]+nums[2]),nums[1])

        for i in range(3,n):
            max_amount[i] = max((max_amount[i-2]+nums[i]),(max_amount[i-3]+nums[i]))

        print(max_amount)
        return max(max_amount[n-1],max_amount[n-2])  
         