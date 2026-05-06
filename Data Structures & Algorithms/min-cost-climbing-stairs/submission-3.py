class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = (len(cost))+1
        cost_stairs = [0]*n
        if len(cost) ==2:
            return min(cost)
        
        cost_stairs[0] = 0

        for i in range(2,n):
            cost_stairs[i] = min(cost_stairs[i-1]+cost[i-1],
            cost_stairs[i-2]+cost[i-2])

        return  cost_stairs[-1]