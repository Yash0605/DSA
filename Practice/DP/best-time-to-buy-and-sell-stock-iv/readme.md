[Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/)

`Prac 1 thought process`:
------------------------------
We need to sell the stock before buying again. We can buy on the same day as selling.
Now as per the pattern we can either buy or sell at a particular day or skip the day entirely.

Skipping the day is dont pi,ck case => straight forward => move to the next index

Picking case => we have 2 options of going ahead
> Case 1 we start from index 0 in this case we will consider we are buying at index 0 and then loop through remaining days to see where we can sell. Now suppose we sell on the day at index 1 this will be 1 trxn => in order to get max val the remaining **subproblem** becomes checking again from index 1 to len(prices).

> Case 2 => we start from end consider index 6 i.e we sell at the last day, then we need to loop through prev indexes to get the day of buying eg consider index 4 and then the **subproblem** becomes checking for the profit from day 4 to day 0

In this pattern we need to check using a for loop inside the recursion. We are checking this because for each index where we either buy or sell we need to check every remaining index to determine if that will yield the maximum profit or not.

`Tabulation`
> What does a cell in the dp table mean
A cell in dp stores the profit till that day => which means we would have sold the stock on that day
        => this means it would have been bought earlier -> thus need to check the profit val for all the earlier days as buying day
        => once the buy day found we will have to consider the subproblem that what was profit till that buying day with 1 lesser trxn
