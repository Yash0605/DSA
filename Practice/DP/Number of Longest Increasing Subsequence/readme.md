# Number of Longest Increasing Subsequence
[Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/)

## Problem Statement

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

## Solution Explanation

In addition to keeping a dp list to get the longest subsequence, we also need to maintain counts list. We will traverse from 0 to i and check if nums[j] < nums[i], then we can have Increasing Subsequence.
Now if dp[j]+1 > dp[i] then we know its a new subsequence from j, so cnt[i] = cnt[j] i.e the count of reaching i will be same as the count of j. In case dp[j]+1 == dp[i] we know that we have already reached the same length subsequence from another element, so we will add the count of num of ways of reaching j to count of num of ways of reaching i.

We need to get the max subsequence length from dp.

Finally we will traverse dp list and add all the counts where we have found dp[i] = max subsequence length => add up all the ways we can get the max subsequence length.

=> Need extra count list and see how we increment or update the count values.