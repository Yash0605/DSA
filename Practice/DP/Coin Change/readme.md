# Coin Change

[Coin Change](https://leetcode.com/problems/coin-change/description/)

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

## Prac 1 thought process

Since we need the minimum we wil have to start from max coin => so sort the coins
In basic recursion we can find the val only with index and amount as varying params
For base recursion => min(pick, dont_pick) because when we say pick an index then that branch is for pick and the other branch is dont_pick
So in above example => [5,5,1] => min is found in the pick branch when we pick 5

Memoization is straight forward

For tabulation => missed the case that we can get the target 0 if we dont pick any coins => so first col will be 0
Secondly for pick case we can pick the same coin again and again so dp[i][j - coins[i]] instead of dp[i-1][j - coins[i]]