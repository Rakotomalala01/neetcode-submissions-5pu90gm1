class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        minute = 0
        fresh = 0
        
        for r in range(rows):
            for c  in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1 :
                    fresh += 1
                
        def addFruit(r, c):
            nonlocal fresh
            if r < 0 or r >= rows or c < 0 or c >= cols :
                return
            if grid[r][c] == 1:
                q.append((r, c))
                grid[r][c] = 2
                fresh -= 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            minute += 1
        return minute if fresh == 0 else -1




        




        