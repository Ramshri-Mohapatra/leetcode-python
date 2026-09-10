"""
1. deque


why not use regualr list - As list.pop(0) is O(n) , 
in BFS we do the operation per node gives O(n^2) so
we use deque ass it give O(1) on bboth ends.
"""

from collections import deque

queue = deque()
queue.append((0,0)) #add to back - O(1)
deque.popleft  # remove from the front - FIFO - O(1)


"""
2.Grid 
This a list of lists

a cell is a tuple of (row,column)

"""

grid = [
    [0,0,1],
    [0,1,1],
    [0,0,0]
]

rows, columns = len(grid), len(grid[0])

"""

3. The 4-directional movement.

Instead of using 4 different if statements for up/down/left/right, 
we store the moves as deltas.

"""

directions = [(-1,0), (1,0), (0,-1), (0,1)] # up, down, left, right

row = 0
column = 0

cell = (row, column)
for dr, dc in directions:
    new_row, new_col = row +dr , column +dc


"""
4. Boundary + visited checking 
Before visiting any cell we must first check three things



if (0 <= new_row < rows and
    0 <= new_col < columns and
    (new_row, new_col) not in visited) :

"""


"""
5. visited - a set of tuples

Why a set and not a list? Same reason as always - O(1) membership check vs O(n) scanning.

why tuples, not two separate variables? Because a tuple (row, col) is "hashable" and can be a 
dict/set key directly — a list can't be (lists are mutable, so Python won't allow them as hash keys).

"""
visited = set()
visited.add((0,0))

(0,0) in visited