"""
Maximum Sum Subarray of Size k

Trigger - Contiguous subarray of fixed/ exact size k

Pattern - sixed size sliding window
"""

def maxSum(num, k):
    left = 0
    windowSum = 0
    result = 0

    for right in range(len(num)):
        windowSum += num[right]
        need = right-left +1

        print(left,right)

        if need > k :
            windowSum -= num[left]
            left+=1
            need = right-left +1


        if need == k:
            result = max(result, windowSum)

    return result


def minSum(nums,k):
    windowSum = 0
    left = 0
    result = float('inf')

    for right in range(len(nums)):
        windowSum += nums[right]
        need = right - left +1

        if need > k:
            windowSum  -= nums[left]
            left += 1
            need = right - left +1

        if need == k:
            result = min(result, windowSum)

       

    return result

nums = [1,9,9,1,1,9]
k = 2

print(minSum(nums,k))


