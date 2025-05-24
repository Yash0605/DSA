# 0 - 1 Knapsack Problem

[0 - 1 Knapsack Problem](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)

Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity.

## Prac 1 thought process

------------------------------
Prac 1 done => for 2D dp check how to form the dp and what will be the sub problem

## Prac 2 thought process

------------------------------

Initially was thinking of sorting and then solving but this was wrong thought process as we cannot get the values if we sort the weights.
Then thought to use pick and dont pick technique as we can pick some weights only based on the W.
Going further with this sol was able to come up with basic recursion
Based on this also came to know that a 2D dp is required for memoization and W will be one of the indexes as it is also is changing and sub problems depend on it and not just the index.
Missed on getting the base cases for tabulation
    => We need to consider W+1 for cols as 0 is also a possible value so we need to start from index 0 and go till W so W+1 cols but return with dp[n-1][W]
    => missed that we can start updating the first row from the col where val = wt[0]
Finally pick and dont pick was same as base recur => still confusion with final return statement
