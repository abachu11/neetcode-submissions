class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        amount,max_amount = 0,0
        l, r = 0,len(heights)-1

        while l<r:
            diff = r-l
            amount = diff*min(heights[l],heights[r])
            max_amount = max(amount,max_amount)

            if heights[l]<heights[r]:
                l = l+1
            else:
                r = r-1

        return max_amount
        