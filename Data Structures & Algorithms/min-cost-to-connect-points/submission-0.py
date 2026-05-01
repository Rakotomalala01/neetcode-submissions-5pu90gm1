class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        in_mst = [False] * n
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        cost = 0

        for _ in range(n): # Because we make n connections 
            curr = -1
            for i in range(n):
                if not in_mst[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
            
            in_mst[curr] = True
            cost += min_dist[curr]

            x1, y1 = points[curr]

            for j in range(n):
                if not in_mst[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[j] = min(min_dist[j], dist)
            
        return cost

        


            
            

