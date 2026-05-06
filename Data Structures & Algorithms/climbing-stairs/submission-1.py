class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        number = [0]*n
        #if n value is 1 0r 2 
        number[0] = 1
        number[1] = 2
        for num in range(2,n):
            number[num] = number[num-1] + number [num-2]

        return number[-1] 