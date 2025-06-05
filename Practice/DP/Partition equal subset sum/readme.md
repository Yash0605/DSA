# Partition Equal Subset Sum

[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

## Prac 1 thought process

Same as target sum => bit easier as we do not have to worry about zeroes in this case
In order to explain why memoization we need to know the following

After drawing the recusrsion tree in the format fn(index, target) and seeing the result we can see that we will have
        overlapping subproblems => hence we will try to memoize
        subset_sum(3, 4)
            ├── subset_sum(2, 4)      ← exclude 1
            │   ├── subset_sum(1, 4)
            │   └── subset_sum(1, 2)
            │       └── subset_sum(0, 2)
            ├── subset_sum(2, 3)      ← include 1 (4-1=3)
                ├── subset_sum(1, 3)
                └── subset_sum(1, 1)
                    └── subset_sum(0, 1)

Once we have the memoized sol then tabulation is easier => only thing we need to check is if we want extra row col or not. In this case since requiredSum can be 0 so we do need it.
