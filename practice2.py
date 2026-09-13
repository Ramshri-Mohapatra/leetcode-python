"""
Given a string s, find the length of the longest substring that contains at most two distinct characters.

Example:
s = "eceba"
Output: 3   ("ece")

"""

def longestK(s):
    left = 0
    stringSize = 0
    n = len(s)
    seen = {}

    for right in range(n):
        seen[s[right]] = seen.get(s[right], 0) +1

        while len(seen) > 2:
            seen[s[left]] -=1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left +=1
         
        stringSize = max(stringSize, right - left +1)
    return stringSize

# s = "eceba"
# print(longestK(s))   

        
"""
Given an array of integers nums, return the length of the longest consecutive elements sequence. The numbers don't need to be contiguous in the array itself — you're looking for consecutive integer values (like 3,4,5), which could appear anywhere in the array, in any order.

Example:
nums = [100, 4, 200, 1, 3, 2]
Output: 4   (the sequence 1,2,3,4)
"""

# def longestSequence(nums):
#     num_set = set(nums)

#     longest = 0

#     for num in nums:
#         if num - 1 not in num_set:
#             length = 1
#             while num + length in num_set:
#                 length +=1
#             longest = max(longest, length)
#     return longest



    
   

# nums = [100,4,200,1,3,2,7,1,8,9,10,12,11]
# print(longestSequence(nums))

            
"""
next

Problem 3

Given the root of a binary tree, return the maximum depth (the number of nodes along the longest path from the root down to the farthest leaf node).

Example tree:
        3
       / \
      9  20
         / \
        15  7

Output: 3

Node definition, in case you need it:

python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

class TreeNode:
    def __init__(self, val =0, left = None, right = None):

        self.val = val
        self.left = left
        self.right = right


node15 = TreeNode(15)
node7 = TreeNode(7)
node9 = TreeNode(9)
node20 = TreeNode(20,node15, node7)


root = TreeNode(3,node9,node20 )

def maxDepth(node):
    if node is None:
        return 0
    left_depth = maxDepth(node.left)
    right_depth = maxDepth(node.right)
    return 1 + max(left_depth,right_depth)

print(maxDepth(root))

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

