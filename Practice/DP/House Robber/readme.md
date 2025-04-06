# House Robber
[House Robber](https://leetcode.com/problems/house-robber/description/)

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

## Solution Explanation

In this problem we just need to use the concept of pick and dont pick. If we pick a house then we can only pick the i+2 house if we start from index 0. 
Ideally we can have many combo that if we pick house 1 then pick maybe house 3 or 4 and so on. All this will be taken care by recursion.
Rest is trust that recursion will give the max val between pick and dont pick.

The time complexity for the **basic recursion solution** (without memoization or tabulation) is **O(2^n)**, where `n` is the number of houses.

### TC Explanation

1. At each house (index), the algorithm has two choices:
   - **Pick** the current house and skip the next one (move to `index + 2`).
   - **Don't pick** the current house and move to the next one (move to `index + 1`).

2. This results in a binary decision tree, where each node represents a recursive call. The depth of the tree is `n` (the number of houses), and at each level, the number of recursive calls doubles.

3. The total number of recursive calls in this binary tree is approximately **2^n**, leading to a time complexity of **O(2^n)**.

### Why is it inefficient?

- The same subproblems are solved multiple times. For example, the result of `helper(nums, index)` is recalculated repeatedly for the same `index`.

### Optimized Solutions

- **Memoization** reduces the time complexity to **O(n)** by storing the results of subproblems in a `dp` array and reusing them.
- **Tabulation** also achieves **O(n)** by iteratively solving the problem from the base cases up to the final solution.
