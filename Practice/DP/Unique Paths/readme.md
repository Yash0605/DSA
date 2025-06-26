# Unique Paths

[Problem Link](https://leetcode.com/problems/unique-paths/description/)

## Prac 1 thought process

---

Tabulation thoughts => A cell in DP signifies the number of possible unique paths that the robot can take to reach that cell. A robot can reach a cell either from its top or its left.
Initial conditions => There is only 1 path for 0th row and 0th col cells.
Based on the above we can see that the number of possible unique paths to reach cell
=> left+top i.e. dp[i-1][j]+dp[i][j-1]

## Prac 2 thought process

---

was able to come up with the logic A robot can reach a cell either from its top or its left. We can have it both ways top and left / bottom and right but bottom and right only works for Memoization. For top and left we need Tabulation. The rest of the logic is simple since we need num ways we add left and top/ bottom and right
