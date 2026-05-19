class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, currSum):
            if currSum == amount:
                return 1

            if currSum > amount or i >= len(coins):
                return 0

            if (i, currSum) in memo:
                return memo[(i, currSum)]

            take = dfs(i, currSum + coins[i])
            skip = dfs(i + 1, currSum)

            memo[(i, currSum)] = take + skip
            return memo[(i, currSum)]

        return dfs(0, 0)