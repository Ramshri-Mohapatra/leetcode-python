"""
Longest Substring Without Repeating Characters


Trigger: Longest substring with no repeats
Pattern: Sliding window + hashmap to detect duplication 
(specifically: shrink when the newly added character's count exceeds 1)

"""

def longestSubstring(s):

    windowSize = 0
    left = 0
    seen_char = {}
    result = 0
    
    

    for right in range(len(s)):
        # print(f"r:{right}")
        # print(f"w: {windowSize}")

        seen_char[s[right]] = seen_char.get(s[right] , 0) +1

        
        # print(d)

        # print(d[s[right]])
        while seen_char[s[right]] > 1:
            seen_char[s[left]] -=1
            left+=1


            # print(f"l:{left}")
            
        windowSize = right -left +1
        result = max(result, windowSize)
        

    return result





"""
Longest Substring with At Most K Distinct Characters


Trigger - Longest substring of distinct K characters

Pattern -  Usliding window + hashmap, shrink while len(hashmap) > k,
 and delete a key from the map only when its count reaches 0 (not just decrement)."

"""

def longestSubstringK(s,k):
    left = 0
    result = 0
    seen_char = {}


    for right in range(len(s)):

        seen_char[s[right]] = seen_char.get(s[right],0) + 1

        while len(seen_char) > k:

            seen_char[s[left]] -= 1
            if seen_char[s[left]] == 0:
                del seen_char[s[left]]
            left+=1

        result = max(result, right - left +1)


    return result


s = "aabbbbcd"
k = 2
print(longestSubstringK(s,k))







