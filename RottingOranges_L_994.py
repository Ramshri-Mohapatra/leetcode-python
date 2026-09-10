"""

Rotting Oranges ( Leetcode 994, Medium)

You're given a grid where each cell is:

0 = empty
1 = fresh orange
2 = rotten orange

Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes until no cell has a fresh orange. If impossible, return -1.

Example:
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
Output: 4

"""
from collections import deque
def rottenOranges(grid):
    if not grid:
     return -1

    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    rotten = set()
    queue = deque()
    fresh = 0

    for r in range(rows):
       for c in range(cols):
          if grid[r][c] == 2:
             queue.append((r,c))
          elif grid[r][c]:
             fresh += 1

    minutes = 0 
             

    while queue and fresh > 0:
       for _ in range(len(queue)):
          row, col = queue.popleft()
          for dr, dc in directions:
             new_row, new_col = row + dr, col + dc
             if(0<= new_row < rows and
                0<= new_col < cols and
                grid[new_row][new_col] == 1):
                grid[new_row][new_col] = 2
                fresh -= 1
                queue.append((new_row, new_col))
       minutes += 1

    return minutes if fresh == 0 else -1

    
         
    
   
grid = [
    [2, 1, 1],
    [0, 0, 0],
    [1, 1, 1]
]
print(rottenOranges(grid))
            

       




    

