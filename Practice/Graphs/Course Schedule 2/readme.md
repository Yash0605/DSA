# Course Schedule 2
[Course Schedule 2](https://leetcode.com/problems/course-schedule-ii/description/

## Problem Statement

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Solution Explanation

The entire solution will be the same as part 1. The only thing we need to track is ordering of the courses.

Part 1 solution:
From problem we can determine this is a directed graph. The only way we cannot take all the courses if there is a cyclic dependency between the courses. So we only need to **find if the graph has a cycle**.

To detect a cycle we will use the algo where we will be **maintaing 2 lists visiting and visited**. Node can either be in visiting list or visited list. If all the neighbors of a node is not visited, it will remain in visiting list, else it will be moved to visited. Now if we come across a node that is already in visiting this means that there is a cycle.

Eg. suppose we have a graph where A => B, B => C and C => A. Now if we start with A we will move it to visiting, and start with node B. Again B will be moved to visiting. We will start with node C and it will also be moved to visiting. Again we reach node A but we can see it is still in visiting hence cycle is present.

We need to traverse all the nodes in the same way we do for disconnected components as we can have a case where courses are not linked.

**For ordering**:
For this we will use the concept of Topological sort/ Kahn's algo. In this if we have nodes u and v and if u is directed to v, we will sort the nodes such that u will preceede v in the sorted list.
For solution persepctive we just need to maintain an extra ans list which will store the sorted nodes/courses. Recusrion stack will then help us to get the ans list.
