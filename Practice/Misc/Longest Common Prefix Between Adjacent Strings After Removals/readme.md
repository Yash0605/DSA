# Longest Common Prefix Between Adjacent Strings After Removals

[Longest Common Prefix Between Adjacent Strings After Removals](https://leetcode.com/contest/weekly-contest-456/problems/longest-common-prefix-between-adjacent-strings-after-removals/description/)

You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

Example 1:

Input: words = ["jump","run","run","jump","run"]

Output: [3,0,0,3,3]©leetcode

## Prac 1 thought process

---

We can have a brute force approach where we traverse outer loop to keep track of removal index and inner loop to check longest common prefix after removing the element at outer loop index, but this will have us check the prefix for same words again and again => not optimal since we know the words from start so its not worth cheking again and again rather we should store it initially and reuse it

Better solution:
At each index we will store the longest common prefix from start to that index => prefixList => This way we know at each index what is the longest common prefix we will get if we check for all the elems prev to it + current index elem
Similarly we will get the longest common prefix val from this index to last index. This way we will get the longest common prefix for all the elems after the current index elem + current elem
Now we can simply traverse and check what is the longest common prefix if the current index ele is removed => that will be the max of all the elem prev to this elem, all the elem after this elem and val for combo of prev and next ele as these are not calculated yet.
