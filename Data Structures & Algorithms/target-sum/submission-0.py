class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curr):
            # Used all numbers
            if i == len(nums):
                # Found valid expression
                if curr == target:
                    return 1
                return 0

            # Already computed
            if (i, curr) in memo:
                return memo[(i, curr)]

            # Choose +
            add = dfs(i + 1, curr + nums[i])

            # Choose -
            subtract = dfs(i + 1, curr - nums[i])

            # Total ways
            memo[(i, curr)] = add + subtract

            return memo[(i, curr)]

        return dfs(0, 0)