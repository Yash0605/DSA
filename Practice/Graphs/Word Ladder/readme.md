# Word Ladder
[Link](https://leetcode.com/problems/word-ladder/description/)

## Problem Statement

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

## Solution Explanation

We will use BFS to get the result. Initially we will form an adjacency list to determine the neighbors for each word. Once we have the neighbors we can do BFS traversal of all the words starting from the beginWord and check if we are able to get the end word.
