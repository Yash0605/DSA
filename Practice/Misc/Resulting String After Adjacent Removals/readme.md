# Resulting String After Adjacent Removals

[Resulting String After Adjacent Removals](https://leetcode.com/contest/weekly-contest-451/problems/resulting-string-after-adjacent-removals/description/?slug=resulting-string-after-adjacent-removals&region=global_v2)

You are given a string s consisting of lowercase English letters.

You must repeatedly perform the following operation while the string s has at least two consecutive characters:

Remove the leftmost pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b', or 'b' and 'a').
Shift the remaining characters to the left to fill the gap.
Return the resulting string after no more operations can be performed.

Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.©leetcode

## Prac 1 thought process

------------------------------
Since we need to check the string again till all the adjacent chars are removed we can choose recursion
But no overlapping subproblems will be available as we need to start fresh after removals
also how to maintain index if the string keeps changing? => Recursion seems to complex

Use combination of while and for loop => while to check if final string found and for to check in current string => This is n^2 solution so will give TLE

Still high TLE => can we have O(n) solution
Since we need to check from left this is similar to parantheses matching problem => This is a classic stack problem
So we can use a stack and compare the current ele to the top of stack and pop from stack accordingly
Easy O(n) solution
