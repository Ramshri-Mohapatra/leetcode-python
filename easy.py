
#contains duplicate

"""
Trigger - Does any Value appear more than once/ check for duplicates

Pattern - HashMap/Set

"""


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

nums2 = []

# print(contains_duplicate(nums1))
# print(contains_duplicate(nums2))

# print(c_duplicate(nums1))
# print(c_duplicate(nums2))


"""
Trigger - Comparing composition/frequency of two containers without order

Pattern - HashMap/Set

Counter - O(n)
For loop - O(m)

so Time complexity = O(n+m) = O(k)

"""



from collections import Counter
def c_anagram(s,t):
  return Counter(s) == Counter(t)
def check_anagram(s, t):
 if len(s) != len(t):
    return False
 s1 = Counter(s)
 t1 = Counter(t)
  
     
 for key in s1:
    if s1[key] != t1[key]:
     return False
         
 return True

s = "anagram"
t = "nagaram" 
s1 = "tar"
t1 = "car" 
# print(c_anagram(s,t))
# print(c_anagram(s1,t1))


  



    
   
   
    


   

    
