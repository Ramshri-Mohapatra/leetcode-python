"""
You're given coin denominations coins and a target amount. Return the minimum number of coins needed to make up that amount. If it's impossible, return -1.

Example:
coins = [1, 2, 5], amount = 11
Output: 3   (5 + 5 + 1 = 11, using 3 coins)

Trigger - Minimum/maximum number of items to reach a specific total

pattern = Build a full dp[] array from 0 to the target, initialized to infinity (unreachable) except 
the base case dp[0]=0. For each amount, try every available option, and take the min() of "solve the 
smaller leftover amount, then add 1 for this choice."

"""


def coinChange(coins, amount):
    dp = [float('inf')] * (amount +1)
    dp[0] = 0

    for a in range(1, amount+1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a-coin] +1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))


