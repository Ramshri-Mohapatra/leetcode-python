
# arr = [1,2,3]
# arr.append(4)
# arr.append(5)
# arr.append(6)
# arr.pop()


# print(arr[0:2]) #here the slicing starts at last element and 5 is out of
#                  #bound hence prints last element

# print(len(arr))



""""

t=(1,2,3)

a,b,c = t
d = {}
d["key"] = 1
d["ram"] = "shri"
d.get("mkey",0)

print(d["key"])

print("key" in d) # membership check, O(1)
print(a,b,c)

for key, value in d.items():
    print(key,":",d[key], sep="")
    print(f"{key}:{d[key]}")

"""

#SET
#s = set() #items inside a data are immutable
#s.add(5)
#5 in s # O(1) look up

"""
#Strings

s = "hello"
s[::-1]
print(s[::-1])

print(list(s))
list_of_characters = list(s)
s1 ="_".join(list_of_characters)
print(s1)

"""
"""
#loops and comprehension
arr = [1,2,3,4]

for i in arr:
    print(i)

for i,value in enumerate(arr):
    print(value, end ="")

print()

doubled_numbers =[x*2 for x in arr] #comprehensions
for i,x in enumerate(doubled_numbers):
    print(x, end="")

"""





