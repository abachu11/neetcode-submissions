class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        amount = [0]*(n)
        amount[0] = nums[0]
        amount[1] = nums[1]
        amount[2] = nums[2]+nums[0]

        for i in range(3,n):
            amount[i] = max(amount[i-2],amount[i-3]) + nums[i]
        print(amount)
        return max(amount[-1],amount[-2])
        