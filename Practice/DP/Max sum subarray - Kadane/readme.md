# Kadane

[Problem Link](https://leetcode.com/problems/maximum-subarray/description/)

## Prac 1 thought process
------------------------------

We need to get the sum from the subarray with max sum. Now as per Kadane we will have to variables `max_till_now` and `max_ending_here`. max_till_now has our required max val and max_ending_here has the max value till the current element.

### 2 cases :
> `mix of positive and negative` => for this we can have the `initial values as 0`. Increment max_ending_here if its greater than 0 else set as 0. Update max_till_now if max_ending_here > max_till_now

> `all negatives` - In this case we cannot have initial values as 0 if the problem states we need to return the element from ths list. In this case if there is minimum 1 ele for the prob we need to set the `max_till_now = nums[0]` => this way we can deal with neg cases.
