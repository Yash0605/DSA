# Wildcard Matching

[Wildcard Matching](https://leetcode.com/problems/wildcard-matching/description/)

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

## Prac 1 thought process

------------------------------

For base recursion was able to come up with the logic and base cases. For the base case we need to keep in mind all the possible scenarios. One diff case is that string has ended and pattern has only * chars left => In this we need to recurse again as we do not know how may * are there and will there be any chars as well

For memoization it is simple only creating the dp and then updating the code accordingly

For Tabulation needed time to come up with the actual table => was not sure if empty row and col is required. But was able to come up with it later.
Earlier missed that if * in pattern we cannot simply consider it to be True => only if its first char then true else we need to get the prev val.
Base case where pattern can be empty was missed => need to consider both pattern and string can be empty
Once knew that empty row and cols were required then it was easy to come up with the iterations.
