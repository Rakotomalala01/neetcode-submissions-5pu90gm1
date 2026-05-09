class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        memo = {}
        # If total is odd, we cannot split it into two equal sums
        if total % 2 != 0:
            return False

        target = total // 2

        # for now, just return target to verify

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i == len(nums) or curr_sum > target:
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            add = dfs(i + 1, curr_sum + nums[i])
            skip = dfs(i + 1, curr_sum)
            memo[(i, curr_sum)] = add or skip
            return memo[(i, curr_sum)]

        return dfs(0, 0)


        
