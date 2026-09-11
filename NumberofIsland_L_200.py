"""
Number of Islands(LeetCode 200, Medium)

Trigger - "Count connected groups/regions" in a grid, "number of islands/clusters," "connected components"
 - the signal is counting separate groups, not finding a shortest path

Pattern - USSe BFS to fin the connected groups and each bfs call is a new group


Example:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from collections import deque
def countIslands(grid):

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    island_count = 0

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited.add((start_row,start_col))
        

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row +dr , col +dc
                if(0<= new_row < rows and 
                   0 <= new_col < cols and
                    (new_row, new_col) not in visited and grid[new_row][new_col] == "1" ):
                    visited.add((new_row,new_col))
                    queue.append ((new_row,new_col))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
              bfs(r,c)
              island_count +=1
                
                

    return island_count


def dfsIslands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count=0

    def dfs(r,c):
        if (r<0 or r >= rows or c<0 or c>=cols or (r,c) in visited or grid[r][c] == "0"):
            return
        visited.add((r,c))
        dfs(r+1,0)
        dfs(r-1,0)
        dfs(r, c+1)
        dfs(r, c-1)
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in visited and grid[r][c] == "1":
                dfs(r,c)
                count+=1
    return count

grid = [
  ["1","1","0","0","1"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(dfsIslands(grid))

