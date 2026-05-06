class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        array = [0] * (len(cost)+1)

        array[0] = 0
        array[0] = 0
        for n in range(2,len(cost)+1):
            array[n] = min(array[n-1]+cost[n-1],array[n-2]+cost[n-2])

        return array[-1]