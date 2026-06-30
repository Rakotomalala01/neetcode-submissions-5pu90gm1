class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tot = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tot += diff
            tank += diff
            if tank < 0:
                start = i+ 1
                tank = 0
        
        return start if tot >= 0 else -1
