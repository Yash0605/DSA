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

## Prac 2:

was not aware of the logic
`2 ways to solve it` => `create the graph with neighbors first` and then check if we get the endWord or not => will give TLE for large input cases as we are creating the graph from the input list and checking for neighbors
Cleaner BFS phase (neighbors are already prepared).
Graph building is very expensive for big word lists (e.g., 5000+ words).
Likely to TLE on large inputs (LeetCode test cases).

`Improved Time complexity way` => we do not create a graph initially rather we create the neighbors on the fly replacing each char with other 25 chars and checking if possible or not => this way we are not limited by the chars in the wordList or number of words. Onluy con is we will end up creating lot of unnecessary words as well

Each word generates L × 26 possible neighbors (L = word length).
Each lookup in word_set is O(1) average (hash set).
Overall runtime: O(N × L × 26), where N = number of words.

Very efficient in practice.
`No need to precompute an entire graph`.
Works well for large wordList.
