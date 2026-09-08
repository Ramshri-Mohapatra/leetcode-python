"""
Subarray Sum equal k
"""

def subArraySumBrute(nums, k):
    count = 0
    n = len(nums)
    

    for start in range(n):
        runningTotal = 0

        for end in range(start,n):
            runningTotal += nums[end]
            
            
            if runningTotal == k:
                print (count)
                count = count + 1

        

    return count


def subArraySum(nums,k):
    count = 0
    prefixSum = 0
    d = {0:1}
    
    for start in range(len(nums)):
        prefixSum += nums[start]
        need = prefixSum - k
        
        print(need)

        if need in d:
            count += d[need]

        d[prefixSum] = d.get(prefixSum,0)+1


       
    print(d.items())

    return count


"""
Here the space complexity is sstill O(n) but time complexity is o(n^2)
"""
def printSubArray(nums,k):

    count = 0
    prefixSum = 0
    d = {0:[-1]}


    for right in range(len(nums)):
        prefixSum += nums[right]
        need = prefixSum - k

        if need in d:

         for start_idx in d[need]:
             subArray = nums[start_idx+1  : right+1]
             print(f"SubArray:{subArray}")
             count+=1

        d.setdefault(prefixSum,[]).append(right)

    return count
             


nums = [3,-3,1,1,1]

print(printSubArray([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))

