class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        change = [[0 for _ in range (amount+1)] for _ in range(len(coins))]

        for i in range(n):
            change[i][0] = 1
            for amount_val in range(1,amount+1):
                if amount_val < coins[i]:
                    change[i][amount_val] = change[i-1][amount_val] if i > 0 else 0
                else:
                    if i ==0:
                        change[i][amount_val] = change[i][amount_val-coins[i]]
                    else:
                        change[i][amount_val] = change[i][amount_val-coins[i]] + change[i-1][amount_val]
                
        print (change)
        return change[n-1][amount]
                    
