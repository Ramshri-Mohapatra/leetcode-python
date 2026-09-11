
def binarySearch(arr,target):
    left, right = 0, len(arr) -1

    while left <= right:
        
        mid = (left + right) //2

        print(right)
        print(left)
        print (mid)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums,target))