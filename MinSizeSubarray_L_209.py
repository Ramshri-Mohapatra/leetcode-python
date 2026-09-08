"""
Trigger - Finding min/max of subarray or sub string to meet condition like 
sum > target
Pattern - Variable size window pattern and have to use while loop to meet 
the condition.

"""

def minSubarray(nums, target):
    windowSum = 0
    left = 0
    result = float('inf')
    best_subarray = []

    for right in range(len(nums)):

        windowSum += nums[right]
        arrayLength = right - left +1
        
        while windowSum >= target:
            # print(nums[left], nums[right])
            windowSum -= nums[left]
            arrayLength = right - left +1
            if arrayLength < result:
                best_subarray = nums[left:right+1]

            left +=1
            # print (arrayLength)
            result = min(result, arrayLength)
        
    print(f"Valid window: {best_subarray} ")
    return result if result !=float('inf') else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7

print(minSubarray(nums,target))

        

        

