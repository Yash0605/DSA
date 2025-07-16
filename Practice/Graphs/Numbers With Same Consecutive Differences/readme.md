# Numbers With Same Consecutive Differences

[Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/)

## Problem Statement

Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

## Solution Explanation

Does not look like a graph problem. There can be multiple ways to solve it one of these is Graph.
We need visualize the sol => suppose n=3 and k=7
This means that we need to find 3 digits number where each digit has difference of 7 with consecutive digits.
In this **for the digits we have 10 options => this will be our nodes => 1,2,3,4,5,6,7,8,9,0**
We have got the nodes, for graph we need some type of relationship between these nodes. For this we will use k. We can connect all the nodes which have a difference of 7 between them. This way 1->8 , 2->9, 7->0.
Using these connections we can traverse all the nodes and form the number by finding the digits at each place.

Eg. 1st digit can only be from 1-9, so we will traverse and check if 1 has any valid connection present. It has in this case so we will add the next digit as 8. Then we will see we need more digits so we will check if 8 has any valid connection present. It has in this case with 1 so we will add 1 to the number. The number has all the required digits so we will add this to answer.

This is only for visualization, actual sol will not require us to form any adjacency list or matrix we can use the DFS traversal and form the number while traversal.

`Prac 2`

Used Brute Force DFS => checked for all the 10 digits for digits other than first digit => This means in the worst case Time Complexity=O(9⋅10^n−1 )
where as for optimized dfs its 2^n as we explore only 2 branches everytime

```python
for i in range(10):
          if abs(current%10 - i) == k:
          getNumbers(index+1, current*10 + i)
```

This is unnecessary loop as we can know which digits can follow after the first one based on value of k => so in worst case here we only check for 2 branches => Significantly better tha checking for all the 10 digits

In both solutions, we only proceed when the digit difference equals k.
So naturally you expect similar time complexity.

`But the key difference isn’t whether we go deeper — it’s how we arrive at those digits.`
Even though it only recurses on digits where abs(current%10 - i) == k, it still:
Checks all 10 digits for each node.
Performs 10 comparisons per node.
Those checks add up across all recursion calls.
