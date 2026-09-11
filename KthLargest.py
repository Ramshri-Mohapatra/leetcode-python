"""

"""


import heapq
def kthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# nums = [3,2,1,5,6,4] 
# k=3
# print(kthLargest(nums, k))


"""
Problem: Top K Frequent Elements (LeetCode 347, Medium)

Given an integer array nums and an integer k, return the k most frequent elements.

Example:
nums = [1,1,1,2,2,3], k = 2

"""
from collections import Counter
import heapq
def topFrequent(nums, k):
    frequency = Counter(nums)
    heap = []
    result = []

    for key, value in frequency.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)

    result = [key for value, key in sorted(heap, reverse = True)]
    
    return result

nums = [1,1,1,1,2,2,3,3,3,4]
k = 3
print(topFrequent(nums,k))