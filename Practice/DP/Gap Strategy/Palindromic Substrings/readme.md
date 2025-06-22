# Palindromic Substrings

[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/)

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

## Prac 1 thought process

We can have the following cases for checking the palindromic substrings:

1. Single character substrings (always palindromic)
2. Two character substrings (check if both characters are the same)
3. Three or more character substrings
   - check if the first and last characters are the same and the substring in between is also a palindrome. We can check if the substring from index `i` to `j` is a palindrome by checking if `s[i] == s[j]` and if the substring from `i+1` to `j-1` is also a palindrome. Eg: "aba" is a palindrome because 'a' == 'a' and the substring "b" is also a palindrome.
   - if the first and last characters are not the same, then it cannot be a palindrome. But we can still check the substring in between for palindromic properties. For this we need to check for 2 cases:
     - i to j-1
     - i+1 to j
       Eg: "abca" is not a palindrome because 'a' != 'a', but we can check the substrings "abc" and "bca" for palindromic properties. If these are palindromic, then we can count them as palindromic substrings.

We can use a nested loop to iterate through all possible substrings and check if they are palindromic. However, this would be O(n^3) in time complexity.

`Basic Memoization`:
We can optimize this by using dynamic programming to store the results of previously checked substrings. We can create a 2D array `dp` where `dp[i][j]` is true if the substring from index `i` to `j` is a palindrome.
We can then iterate through the string and fill in the `dp` array based on the above cases. Finally, we can count the number of palindromic substrings by iterating through the `dp` array.

`Gap Strategy`:
In normal DP we would have used a 2D array to store the results of previously checked substrings. But here the result does not depend on the previous results. In this case we need to traverse diagonally which is length wise.
In this case we only have 1 string so it will be placed in both row and col. We will traverse length wise i.e we will check substrings of length 1, then length 2, then length 3 and so on. Suppose we are checking for length 4 "abca" => here a == a so we can check the substring "bc" in between since its length is 2, we would have already checked for length 2 substrings. So we can use the results of the previous checks to determine if the current substring is a palindrome or not.
Also we only need to check for upper diagonal cells as cells below the diagonal represents reverse sub strings and we need to check for those here.

For our loop => length => 1-n and i => 0 - n-length
j = i+length-1
s = "abccba" => n = 6
So for length = 1 => i goes from 0 - (6-1) = 0 - 5
=> j = 0+1-1 = 0 so (0,0) traversed
=> j = 2+1-1 = 2 so (2,2) traversed
=> j = 3+1-1 = 3 so (3,3) traversed
=> j = 4+1-1 = 4 so (4,4) traversed
=> j = 5+1-1 = 4 so (5,5) traversed
=> All strings of length == 1 traversed

So for length = 3 => i goes from 0 - (6-3) = 0 - 3
=> j = 0+3-1 = 2 so (0,2) traversed
=> j = 1+3-1 = 3 so (1,3) traversed
=> j = 2+3-1 = 4 so (2,4) traversed
=> j = 3+3-1 = 5 so (3,5) traversed
=> All strings of length == 3 traversed and so on

In this case we do not explicitly check for cases where length>2 and s[i]!=s[j] => As per logic we should check for i to j-1 and i+1 to j but we need to keep in mind if the substrings are palindromic they would have already been considered as they are of lesser length.
