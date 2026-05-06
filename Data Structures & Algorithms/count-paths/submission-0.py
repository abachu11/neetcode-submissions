from math import factorial as fact
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m + n -2
        return int(fact(total_steps) / (fact(m-1)*fact(n-1)))