# Count Square Submatrices with All Ones

## Problem Statement

Given an `m x n` matrix of ones and zeros, return how many square submatrices have all ones.

## Solution Explanation

### Approach

The solution uses dynamic programming to count the number of square submatrices with all ones. The idea is to use a DP table where `dp[i][j]` represents the size of the largest square submatrix ending at position `(i, j)`.

### Steps

1. **Initialization**:
   - Create a DP table `dp` initialized with the same values as the input matrix.
   - Initialize a variable `ans` to store the total count of square submatrices with all ones.

2. **DP Table Update**:
   - Iterate through the matrix starting from the second row and second column.
   - For each cell `(i, j)`, if the value is `1`, update `dp[i][j]` to be the **minimum of the values from the top, left, and top-left diagonal cells plus one**.
   - This update ensures that `dp[i][j]` contains the size of the largest square submatrix ending at `(i, j)`.
   - Update the ans value with the current value of `dp[i][j]`

## Time Complexity: O(n*m)

## Space Complexity: O(n*m)
