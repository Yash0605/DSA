# Network Delay Time
[Network Delay Time](https://leetcode.com/problems/network-delay-time/description/

## Problem Statement

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

![Problem image](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

## Solution Explanation

**Dijkstar's Algo**:

This is a **greedy solution**, at each step we will find which is the min weighted edge and consider that edge, till we traverse all the nodes.

We will use **priority queue and a distance list** to store the current min values => push the source in the queue and then with BFS traversal we will traverse all the neighbors and add to the priority queue. The Priority queue will have the min value at the top using this we will traverse its neighbors and update the distance list if we get the minimum value.

Time Complexity : **O(Elog(V))** => log(V) because of priority queue which uses heap data structure. This is an improvement over the Bellman Ford Algo which was O(V*E)

