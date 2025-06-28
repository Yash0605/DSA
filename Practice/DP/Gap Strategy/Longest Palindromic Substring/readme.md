# Longest Palindromic Substring

[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/)

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

## Prac 1 thought process

---

For the recursive solution we need to find the palindromic substrings and then check if they are longer than already encountered substring. For this we need to keep a variable which checks whether current substring being checked is palindromic or not.
We have following cases if palindrome:
=> 1 char => base case
=> 2 chars => need to check if both char same or not
=> if i and j chars are same => in this case need to check i+1 and j-1 length substring is palindrome or not => if palindrome check length if greater then probable candidate

else if not above cases we need to check if
=> i+1, j substring palindrome or not
=> i, j-1 substring as well

Tabulation sol:
length => 1 - n
i => 0 - n-length+1
j = i+length-1

again check if we have any valid case => then consider as probable candidate
