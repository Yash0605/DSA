# Min Cost to Connect All Points
[Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)

## Problem Statement

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

![Prob image](https://assets.leetcode.com/uploads/2020/08/26/d.png)

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

![Sol image](https://assets.leetcode.com/uploads/2020/08/26/c.png)

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

## Solution Explanation

Since we need exactly 1 simple path, we can achieve this via creating a minimum spanning tree. We can use either Prim or Kruskal Algo.

In Prim's Algo we will have to use BFS using priority queue implementation, we will have to get the distance b/w all the points and using the distance priority queue will give the desired tree.

Kruskal's algo => we will have to create to create the edges Data structure which needs to be sorted as we need the min edge to start with. Following this we will have the Disjoint Set implementaion which has the Union and findParent methods that can help us to get the desired tree.