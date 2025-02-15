# Best time to buy and sell stock 2

[Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

`Prac 1 thought process`
------------------------------

For the **tabulation** method => we will check what is the **profit we can get if we sell the stock on ith day**.
In the dp list each cell signifies what would be the profit if the stock was bought at any of the earlier days and then sold at this ith day
    so j loop runs to traverse the prev buying days and check which day could yield the max profit
    but this would only make sense if current day price is greater than prev day price else we would already have the max profit 
        - no need to check then at the current index hence the if condition

How is it different from Best time to buy and sell stock 4:
In the Best time to buy and sell stock 4 case we are also given the number of possible trxns whereas here we only have 1 trxn at a time but we can make any number of trxns => hence only 1D dp required rather than a 2D one.

But this is not the final solution since it still has a higher time complexity -  we can still reduce it to a lower time complexity
**Mathematical sol** =>
Suppose we have a increasing array => [1,3,5,7,9] => In this case profit will be when we do 9-1 = 8.
But we can get the same ans if we do => 3-1+5-3+7-5+9-7 = 8
Thus we can get the same val if we just do profit+=prices[i] - prices[i-1] for the case where prices[i] > prices[i-1]
In case we get a decreasing sequence we can simply skip it and still get the same ans

