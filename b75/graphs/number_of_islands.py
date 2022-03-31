class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visit.add((row, col))
            
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row in range(rows)) and (col in range(cols)) and ((row, col) not in visit) and grid[row][col] == '1':
                            q.append((row, col))
                            visit.add((row, col))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and ((r,c) not in visit):
                    bfs(r, c)
                    islands += 1
        return islands