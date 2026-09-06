
#contains duplicate
def c_duplicate(nums):
   return len(nums) != len(set(nums)) #no early exit as we build the whole set

def contains_duplicate(nums):  #can early exit so better average case performance
  s = set()
  for i in range(len(nums)):
      if nums[i] in s:
         return True
      s.add(nums[i])
  return False

nums1 = [1,2,3,1]

nums2 = [1,2,3,4]

print(contains_duplicate(nums1))
print(contains_duplicate(nums2))

print(c_duplicate(nums1))
print(c_duplicate(nums2))


    


   

    
