"""
Two Sum with input array sorted 
Given a 1-indexed array of integers numbers that is already sorted 
in non-decreasing order, find two numbers such that they add up to 
a specific target. Return the indices (1-indexed) of the two numbers.

Trigger: "Pair sum equals target, array is sorted" the sortedness is
 the critical trigger word; without it, you'd default to HashMap instead.

Pattern: Two pointers from both ends — move left right if sum is too small,
move right left if sum is too big.

"""

def twoSum(nums, target):

    left = 0
    right = len(nums) - 1
    

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left  ,right] # to return +1 indices values
        elif sum < target:
            left +=1
        else:
            right-=1

    return []




# print(twoSum(numbers,target))


def c_twoSum(nums,target):
    seen ={}
    result = []

    for right in range(len(nums)):
        complement = target - nums[right]
        if complement in seen:
            result.append([seen[complement],right])
        seen[nums[right]] = right
    print(seen)

    return result


sortedArray = [0,1,2,3,4,5,6]



"""
Three Sum value based output
"""

def threeSum(nums, target):
    nums.sort()
    result = []


    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i +1, len(nums) -1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                left +=1
                right-=1
                while left < right and nums[left] == nums[left-1]:
                    left +=1
            elif total < target:
                left+=1
            else:
                right-=1

    return result

numbers = [0,3,3,3,3,6,4,5]
target = 9
print(twoSum(numbers, target))



"""
This function finds the indices of three elements that sum up to a target
but here the input array needs to have no duplicates for it to give the 
indices value as with duplicate values its not possible to store the indices 
of these value in a hashMap.
"""
"""
def twoSumHelper(nums, target):

    left = 0
    right = len(nums) - 1
    result = []
    

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            result.append([nums[left] ,nums[right]])
            left+=1
            right-=1
        elif sum < target:
            left +=1
        else:
            right-=1

    return result


def threeSum(nums, target): 

    first = 0
    second = 0
    third = 0
    d = {}
    output = []
    list = []
    n = len(nums)
    for right in range(len(nums)):  #ddoesnt work if array has duplicates
        d[nums[right]] = right

    sortedArray = sorted(nums)

    for right in range(len(sortedArray)):
        print(sortedArray[right])
        complement1 = target - sortedArray[right]

        result = twoSumHelper(sortedArray[right+1:n+1], complement1)
        print(result)
        for i in range(len(result)):
          second, third = result[i]
          list.append([sortedArray[right], second, third])

    for i in list:
        first, second, third = i
        output.append([d[first],d[second],d[third]])
        

    return output

print(threeSum(numbers,target))

"""

        
        
        
        
            
    

             
            

    


    



