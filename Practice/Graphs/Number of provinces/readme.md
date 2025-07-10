# Number of Provinces

[Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)

## Problem Statement

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where `isConnected[i][j] = 1` if the ith city and the jth city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

## Solution Explanation

We need to be aware that we can have `components` in this case. We need to traverse each node and update the num of province everytime we come across a disconnected node.
We need to DFS as we need to check all the connected nodes for a particular node so go deep considering each node rather than traverse breadth wise.

> Prac2

We only need to mark the nodes as visited and traverse all the nodes to track the components => basic dfs
