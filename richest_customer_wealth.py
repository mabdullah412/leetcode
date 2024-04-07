class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])

        wealth = []
        for i in range(m):
            wealth.append(0)

        for i in range(m):
            for j in range(n):
                wealth[i] += accounts[i][j]
        
        maxw = wealth[0]
        for i in range(m):
            if wealth[i] > maxw:
                maxw = wealth[i]

        return maxw