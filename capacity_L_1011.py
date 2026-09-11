"""
Capacity To Ship Packages Within D Days (LeetCode 1011, Medium)

You have weights — an array of package weights, in the order they must be shipped. You must ship them in days days, using a ship of some fixed weight capacity. Each day, load as many packages as fit (without exceeding capacity), in order, without splitting a package.

Find the minimum ship capacity that allows shipping all packages within days days.

Example:
weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15

Trigger - "Find the minimum/maximum value X such that some condition holds" — 
phrases like "minimum capacity," "minimum time," "smallest value such that,
" "maximum such that Y is still possible."

pattern - Binary search over the range of possible answers (not the array 
itself) — write a checker function that says 'does this candidate value 
satisfy the condition,' then binary search using left < right, right = mid 
(keep working answers), left = mid + 1 (discard failures), converging on 
the smallest value that works."
"""

def checkCapacity(weights, capacity, days):
    days_needed = 1
    current_load = 0

    for weight in weights:
        if current_load  + weight > capacity:
            days_needed +=1
            current_load = 0
        current_load += weight

    return days_needed <= days

def shipWithinDays(weights,days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        if checkCapacity(weights, mid, days):
            right = mid
        else:
            left = mid + 1

    return left
        

    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(shipWithinDays(weights, days))
            
       
        

