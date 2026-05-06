class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        def sumOfSquares(n):
            result = 0
            while n:
                digit = n%10
                result += digit**2
                n = n//10
            return result

        while n not in visit:
            visit.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        return False

    

