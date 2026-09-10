
# arr = [1,2,3]
# arr.append(4)
# arr.append(5)
# arr.append(6)
# arr.pop()


# print(arr[0:2]) #here the slicing starts at last element and 5 is out of
#                  #bound hence prints last element

# print(len(arr))



""""

t=(1,2,3)

a,b,c = t
d = {}
d["key"] = 1
d["ram"] = "shri"
d.get("mkey",0)

print(d["key"])

print("key" in d) # membership check, O(1)
print(a,b,c)

for key, value in d.items():
    print(key,":",d[key], sep="")
    print(f"{key}:{d[key]}")

"""

#SET
#s = set() #items inside a data are immutable
#s.add(5)
#5 in s # O(1) look up

"""
#Strings

s = "hello"
s[::-1]
print(s[::-1])

print(list(s))
list_of_characters = list(s)
s1 ="_".join(list_of_characters)
print(s1)

"""
"""
#loops and comprehension
arr = [1,2,3,4]

for i in arr:
    print(i)

for i,value in enumerate(arr):
    print(value, end ="")

print()

doubled_numbers =[x*2 for x in arr] #comprehensions
for i,x in enumerate(doubled_numbers):
    print(x, end="")

"""



"""
subArray of lenght k
"""

# def subArray(nums, k):
#     count = 0
#     prefixSum = 0
#     d = {0:[-1]}
#     result = []

#     for right in range(len(nums)):
#         prefixSum += nums[right]
#         need = prefixSum -k

#         if need in d:
#             for start_index in d[need]:
#                         subArray = nums[start_index+1: right+1]
#                         result.append(subArray)
#                         count+=1
            

        
#         d.setdefault(prefixSum, []).append(right)
        


        
#     print(result)
#     return count


# print(subArray([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))

"""
Two Sum

"""

# from collections import defaultdict
# def twoSum(nums, target):

#     seen = defaultdict(list)
#     result = []

#     for i in range(len(nums)):
#         complement = target - nums[i]

#         if complement in seen:
#             for prev_indx in seen[complement]:
#                 result.append((prev_indx,i))

#         seen[nums[i]].append(i)
#     print(seen)
#     return result

# def twoSum_v2(nums, target):  # for sorted
#     left = 0
#     right = len(nums) - 1
#     result = []

#     count = 0

#     while left < right:

#         sum = nums[left] + nums[right]

#         if  sum == target:
#             count +=1
#             result.append((left, right))
#             left+=1
#             right -=1
#         elif sum < target:
#             left+=1
#         else:
#             right-=1
#     print(result)
#     return count 



# nums = [1,2,3,4,5,6]
# target = 9

# print(twoSum_v2(nums,target))

"""
Maximum sum of array of fixed size K


"""
# def maxSum(nums, k):
#     left = 0
#     windowSum = 0
#     result = 0

#     for right in range(len(nums)):
#         windowSum += nums[right]
#         need = right -left +1

#         if need > k:
#             windowSum -= nums[left]
#             left +=1
#             need = right -left +1

#         if need == k:
#             result = max(result, windowSum)
#     return result
    
# nums = [1,9,9,1,1,9]
# k = 2

# print(maxSum(nums,k))


"""
LeetCode 209 is Minimum Size Subarray Sum
"""

# def minSubarray(nums, target):

#     left = 0
#     windowSum = 0
#     result = float('inf')

#     for right in range(len(nums)):
#         windowSum += nums[right]
    

#         while windowSum >= target:
#             result = min(result, right-left+1)
#             windowSum -= nums[left]
#             left+=1
            
        
#     return result if result != float('inf') else 0

# target = 7
# nums = [2, 3, 1, 2, 4, 3]

# print(minSubarray(nums, target))

"""
LeetCode 3 is Longest Substring Without Repeating Characters.


"""

# def longestSubstring(s):

#     left = 0
#     windowSize = 0
#     result = 0
#     seen = set()

#     for right in range(len(s)):
        

#         while s[right] in seen:
#             seen.remove(s[left])
#             left +=1
#         seen.add(s[right])
#         windowSize = right - left +1

#         result = max(result, windowSize)
#     return result


# s = "bbbb"
# print(longestSubstring(s))


"""
LeetCode 340 is Longest Substring with At Most K Distinct Characters
"""
        
# def distinctK(s, k):

#     left = 0
#     seen = {}
#     result = 0
#     windowsize = 0

#     for right in range(len(s)):

#         seen[s[right]] = seen.get(s[right], 0) +1
#         while len(seen) > k:
#             seen[s[left]] -=1
#             if seen[s[left]] == 0:
#                 del seen[s[left]]
#             left +=1
            

#         windowsize = right -left +1
        
#         result = max(result, windowsize)

#     return result


# s = "eceba"
# k = 2

# print(distinctK(s,k))

"""
Three Sum
"""

# def threeSum(nums, target):
#     nums.sort()
#     result = []


#     for i in range(len(nums)):

#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         right = len(nums) -1
#         left = i +1

#         while left < right:

#             if nums[left] + nums[right] == target - nums[i]:
#                 result.append((nums[i], nums[left], nums[right]))
#                 left +=1
#                 right -=1
#                 while left < right and nums[left] == nums[left-1]:
#                     left+=1
#             elif  nums[left] + nums[right] >  target - nums[i]:
#                 right -=1
#             else:
#                 left +=1

#     return result

# numbers = [1, 2, 2, 5, 5]
# target = 8

# print(threeSum(numbers, target))


"""
LeetCode 200 is Number of Islands.The Problem DescriptionGiven an m x n 2D 
binary grid grid which represents a map of '1's (land) and '0's (water),
return the total number of islands.An island is surrounded by water and 
is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are completely surrounded by 
water.
"""

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# from collections import deque

# def noofIslands(grid):

#   if not grid:
#      return 0
  
  
#   rows, cols = len(grid), len(grid[0])
#   directions = [(-1,0), (1,0), (0,-1), (0,1)]
#   visited = set()
#   step = 0

#   def bfs(start_row, start_col):
#     queue = deque([(start_row, start_col)])
#     visited.add((start_row,start_col))

#     while queue:
#       row, col = queue.popleft()
#       for dr, dc in directions:
#         new_row, new_col = row +dr, col +dc
#         if (0<= new_row < rows and
#             0<= new_col < cols and
#             (new_row, new_col) not in visited and grid[new_row][new_col] == "1"):
#           queue.append((new_row,new_col))
#           visited.add((new_row, new_col))

#   for r in range(rows):
#     for c in range(cols):
#       if grid[r][c] == "1" and (r,c)not in visited:
#         bfs(r,c)
#         step+=1

#   return step

# print(noofIslands(grid))
# print(noofIslands(grid2))



    
"""
LeetCode 994 is Rotting Oranges
"""
grid = [
    [2, 1, 1, 2],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]
from collections import deque
def rottingOranges(grid):

    fresh = 0
    directions = [(-1,0), (1,0), (0,-1),(0,1)]
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    minutes = 0


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            if grid[r][c] == 1:
                fresh+=1
    # print(fresh)

    while queue and fresh > 0:
        # print(queue)
        for _ in range(len(queue)):
            # print(fresh)
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col +dc
                if(0 <= new_row < rows and 
                   0 <= new_col < cols and
                   grid[new_row][new_col] == 1):
                    grid[new_row][new_col] = 2
                    
                    queue.append((new_row,new_col))
                    # print(queue)
                    fresh-=1
        minutes +=1

    return minutes if fresh == 0 else -1

print(rottingOranges(grid))










