# Target Sum

[Target Sum](https://leetcode.com/problems/target-sum/description/)

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

## Prac 1 thought process

------------------------------

Prac 1 done => check which DS can be used for DP => if not reducing the problem to subset sum then we will have
to use a dict as target can be negative.

## Prac 2 thought process

------------------------------

Missed the math logic that we can use to reduce it to a subset problem=> secondly once it is reduced to a subset problem we need to consider the case with 0's as num of ways we can achieve a target will be doubled with 0 as an element.
**Using Maths and subset**
We know that some ele can have +ve operator and some can have -ve operator
So nums can be divided in 2 subsets
    - P => has all the ele with positive values
    - N => has all the ele with negative
    P+N = total
    P-N = target -. as per the problem
    Eg:[1,1,1,1,1] => P = ele at [0,2,3,4]
                    => N = ele at [1]
                    => if target = 3 => then can be achieved by P-N

    P+N = total
    P-N = target
    2P = total+target
    P = (total+target)/2
    Thus this comes down to finding how many such subsets exists
