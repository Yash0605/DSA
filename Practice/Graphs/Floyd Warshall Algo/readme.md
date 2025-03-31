# Network Delay Time
[Network Delay Time](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

## Problem Statement

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

## Solution Explanation

Floyd Warshall algo helps to find the shortest distance of node u from all the other nodes in the graph. This is a DP solution. Uses adjacecny matrix. We try to to reach Node v from Node u via Node A. Initially all cells set to inf except for diagonal which will be 0. Then start filling via all the nodes.
Eg: distance(AD) = min(dist(AD), dist(AB)+dist(BD)) => where B is a node between A and D.
