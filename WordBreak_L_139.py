"""
Leetcode 139 WordBreak

Trigger - Is it possible to seperate a string into substring in the dictionary

pattern = build the dp for prefix and check remaining substring is a valid dictionary word
then whole string is valid

"""

def wordBreak(s, wordDict):
    dict = set(wordDict)
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range (i):
            if dp[j] and s[j:i] in dict:
                dp[i] = True
                break

    return dp[n]

s = "leetcode"
wordDict = ["leet", "code"]

s1 = "catsandog"
wordDict1 = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s1, wordDict1))