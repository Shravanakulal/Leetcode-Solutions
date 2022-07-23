class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
            
        for i in accounts:
            curr_wealth = sum(i)
            if curr_wealth > max_wealth:
                max_wealth = curr_wealth 
                
        return max_wealth     