class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return 0
        step_cost = [0]*(n+1)
        step_cost[0] = 0
        step_cost[1] = 0

        for i in range(2,n+1):
            step_cost[i] = min((step_cost[i-1]+ cost[i-1]), (step_cost[i-2]+cost[i-2]))

        return step_cost[-1]