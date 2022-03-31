class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []
        
        def dfs(row, column, visit, prevHeight):
            if (row, column) in visit or (row < 0) or (column < 0) or (row == ROWS) or (column == COLS) or (heights[row][column] < prevHeight):
                return
            visit.add((row, column))
            dfs(row + 1, column, visit, heights[row][column])
            dfs(row - 1, column, visit, heights[row][column])
            dfs(row, column + 1, visit, heights[row][column])
            dfs(row, column - 1, visit, heights[row][column])
                
        
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS-1, col, atlantic, heights[ROWS-1][col])
            
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS-1, atlantic, heights[row][COLS-1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
                    
        return res