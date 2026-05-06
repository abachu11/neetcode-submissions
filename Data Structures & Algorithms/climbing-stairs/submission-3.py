class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        array = [0]*n
        #if  n = 1 or 2
        array[0]  = 1
        array[1] = 2
        for num in range(2,n):
            array[num] = array[num-1] + array[num-2]
        
        return array[-1]     
        