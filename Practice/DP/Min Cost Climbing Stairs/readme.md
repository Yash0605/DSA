# Min Cost Climbing Stairs
[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

## Problem Statement

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.

- Pay 15 and climb two steps to reach the top.

The total cost is 15.

## Solution Explanation

In this we need to find the min cost of reaching the top floor, which means if cost has 3 elements there will be 4 steps in total and we need to reach the 4th step.
We can either start from 1st step i.e 0th index or directly start from 2nd step which is 1st index.
Now if we need to find the **cost of reaching 3rd step =>** 
**min(cost of reaching 1st step+cost of 1st step, cost of reaching 2nd step+cost of 2nd step)**
Why cost of 1st step => because to reach the 3rd step we will jump from 1st step in this case so cost of jumping needs to be added as well.

**There can be confusion as if we give calc for n=2, we can think it means 2nd step but this actually refers to 3rd step. 2 is for index in cost list so actually means the 3rd step. This will help us to understand the solution.**

But Basic Recursion will be TLE.

Memoization is straight forward using extra dp list

Tabulation can cause confusion as we consider i from 2 so does it mean 2nd step? =. As mentioned above this would give sol for reaching the 3rd step. Also directly jumping to space optimized Tabulation seems confusing so it would help if we understand the tabulation with dp list before.
