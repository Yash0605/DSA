# Matrix Chain Multiplication

[Link](https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1)

## Problem Statement

Given an array arr[] which represents dimensions of sequence of matrices where the ith matrix has the dimensions `(arr[i-1] x arr[i])` for i>=1., find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

## Solution Explanation

In this problem we need to find the efficient way to multiply these matrices together, so for this we will have to divide the given list in different ways. So we will have partitions for the list and with each partition the list length will be reduced. Hence we can have use the Gap strategy to solve this problem.

### Steps
arr = [40, 20, 30, 10 ,30] => this has 4 matrices => `40*20 , 20*30, 30*10, 10*30`
So for Gap strategy sol we can traverse from 1st index till the last index i.e from i=1
We have 3 cases
1> length=1: If only 1 matrix is present then cost of mul = 0

2> length=2: We have 2 matrices => so val = `arr[i-1]*arr[i]*arr[j]` i.e if first 2 matrices considered `40*20*30`

3> length>2: Here we have the need for partitions => Suppose we have matrices A,B and C. We can divide as AB and C or A and BC. Accordingly k will go from i to j and `dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j])`


## Time Complexity: 

## Space Complexity: