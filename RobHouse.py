def bestRob(house):

    prev2, prev1 = 0 , 0 # no house robbed

    for i in house:
        current = max(prev1, prev2 + i)
        prev2 = prev1
        prev1 = current

    return prev1

nums = [2,7,9,3,1]

print(bestRob(nums))