# Cheapest Flights Within K Stops
[Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

## Problem Statement

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

![Problem 1](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

## Solution Explanation

We will have to use the Shortest path algo, but here we have restriction that we need k stops. So we cannot use Dijkstra as it will give us the final shortest path rather than with the given restriction. We can use Bellman Ford Algo as it uses relaxations to get the min distance after each ith relaxation. So we can leverage this and set the number of relaxation to the given value of stops.
