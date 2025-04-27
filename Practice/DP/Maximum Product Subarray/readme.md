# Maximum Product Subarray

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

## Prac 1 thought process
------------------------------
There are 2 ways to solve the problem => dp way and logical way => as per the comments logical way is difficult to explain in an interview if the interviewer is not aware of the logic.

For this problem we have 4 cases:
> All posistive w/o zeroes
> Even negatives w/o zeroes
> Odd negatives w/o zeroes
> Zeroes

**Logical way** => For first 2 cases we can simply traverse the list and get the product. For the case of 0 we can have the product with subarrays on either side of zero.

If we check in case of odd negatives we can either select the 1st element or the last element so that we have even number of negatives.
So we will start the traversal from both start and end of the list. This way we will maintain a prefix and suffix value. For prefix we will maintain the product from the start and for suffix we will cal product from n-1 element. At each pass we will calc the max value.

**DP Way** => We will maintain 2 values again but in this case it will be current max and current min. At each index either of the values can become max based on negative number.
Base logic is that if a big number is multiplied with a neg number then ans is a smaller number => pos*neg
if a smaller number is multiplied with a neg number then ans is a bigger number => neg*neg
We will maintain 2 variables currentMin and currentMax
3 cases => no 0 and odd neg
        => no 0 and pos neg => same as all pos
        => has 0 => then ans would be some subarray
swap in case the current value is negative => currentMax,currentMin = currentMin, currentMax
This will help us to get the max value at each step.
For the case of 0, we will ste the vals as 0 so essentially the values will be reset and the calc will start again from the next index:
currentMax = max(nums[i], currentMax*nums[i])
currentMin = min(nums[i], currentMin*nums[i])

