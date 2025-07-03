# Longest Palindromic Subsequence

[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/)

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

## Prac 1 thought process

---

Initial thought from looking at the example was how can we remove the char which will not be part of palindrome i.e how to remove 'a' and then consider 'bbbb' and this led to pick dont pick scenarios.

But this is wrong direction to think

=> we can use the strategy where we traverse from start and end

=> check if s[i] == s[j] and if so we check for sub problem i.e `2 + fn(i+1 and j-1)` => 2 as we have already found 2 chars i and j which are equal so even if none of the chars in the subproblem is same we can still have the ans as 2 => This way removal of chars is taken care of => no pick dont pick scenarios required

=> if s[i] != s[j] => we can check for the `max(fn(1,j-1) and fn(i+1, j))` => This way we skip the i or j elems and check if subproblems has any palindrome. Recursion takes care of removal as we get 0 if we dont get the common chars
