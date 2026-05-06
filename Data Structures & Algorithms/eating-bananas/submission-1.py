from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        len_piles = len(piles)

        if h == len_piles: 
            return r
        l = 1
        while l <= r:
            k = (l+r)//2
            time_k = 0
            for val in piles:
                time_k += ceil(val/k)

            if time_k > h:
                l = k+1
            else:
                res = k
                r = k - 1 

        return res
