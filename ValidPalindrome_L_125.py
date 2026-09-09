"""
Valid Palindrom

Trigeer - check for valid palindrome

Pattern - Clean the string and compare reverse but here space complexity O(n)
        - Better to use two pointers as no new string to be made hence space 
        complexity wil be o(1)
"""

import re

def validPalindrome(s): #space O(n)

    cleaned_string = "".join(char for char in s if char.isalnum()).lower()
    print(cleaned_string)
    print(cleaned_string[::-1])

    lower_s= s.lower()

    cleaned_s = re.sub(r'[^a-z0-9]','', lower_s) # use regex
    

    if cleaned_string == cleaned_string[::-1]:
        return True

    return False

s = "A man, a plan, a canal: Panama"



def validPalindromeTwoPointers(s):  #space o(1)

    left = 0
    right = len(s)-1

    while left < right:
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1




    return True

print(validPalindromeTwoPointers(s))