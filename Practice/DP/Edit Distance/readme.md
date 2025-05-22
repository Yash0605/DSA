# Edit Distance

[Edit Distance](https://leetcode.com/problems/edit-distance/)

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

## Prac 1 thought process

------------------------------
prac1 done => check how we get tabulation cell values

## Prac 2 thought process

------------------------------
prac2 done - able to come up with the logic but missing how to implement it
=> knew how indexes will behave for same chars and replace, del and ins cases but not sure how to handle the return for same and diff characters => trust the process that recusrsion will take care of the rest of the problem, we only need to solve for the current subproblem
=> knew the base conditions but again missed on correct implementation => how to calculate the values when either one of the words pass their indexes 
=> in case of memoization had set incorrect row and col values for creations 
    => dp = [[-1]*m for i in range(n)] => [-1]*m maps to second index and is our column
=> Tabulation is easier once able to form the logic for base recusrion => keep in mind to use the extra row col for base case
