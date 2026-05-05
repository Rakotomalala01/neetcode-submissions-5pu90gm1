class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visit= set()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minH = [[grid[0][0], 0, 0]]

        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == rows - 1 and c == cols - 1 :
                return t
            for dr, dc in dir:
                neiR, neiC = r + dr, c + dc
                if neiR < 0 or neiC < 0 or neiR == rows or neiC == cols or (neiR, neiC) in visit:
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
            
        


            


        