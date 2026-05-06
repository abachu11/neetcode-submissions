class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1,1

        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            temp = currMin
            currMin = min(currMin*n, currMax*n, n)
            print('For iteration the min value is ',currMin,n)
            currMax = max(currMax*n, temp*n, n)
            print('For iteration the max value is ',currMax,n)
            
            res = max(res, currMax)

        return res