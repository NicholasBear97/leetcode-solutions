class MaxWealth:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        #return the max of lists of lists' sums
        return max([sum(acc) for acc in accounts])
