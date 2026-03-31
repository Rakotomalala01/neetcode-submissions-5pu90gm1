class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []

        def dfs(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            if tot > target or i >= len(nums):
                return 
            
            cur.append(nums[i])
            dfs(i + 1, cur, tot + nums[i])
            cur.pop()
            while i+ 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur, tot)
        
        dfs(0, [], 0)
        return res