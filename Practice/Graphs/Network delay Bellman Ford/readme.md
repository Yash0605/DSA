# Network Delay Time
[Network Delay Time](https://leetcode.com/problems/network-delay-time/description/

## Problem Statement

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

![Problem image](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

## Solution Explanation

**Bellman Ford Algo**:

Firstly we have concept of **relaxation** which is: suppose we are going from node 2 to node 4. In this case the distance will be:

distance(2,4) = distance(3) + distance(3,4)

This is relaxation. DP approach to find the min distance.

The algo states that if we apply relaxation to all the edges nodes-1 time then we should be able to get the shortest distance between given source and destination.

Time Complexity : O(V*E) => we know E = n(n-1)/2

so T.C~O(N^3)

Easier to implement but high T.C 
