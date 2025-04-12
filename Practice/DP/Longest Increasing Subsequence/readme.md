# LIS:

[Problem Link](https://leetcode.com/problems/longest-increasing-subsequence/description/)

`Prac 1 thought process`
------------------------------

This is the case of 1D dp. For each ele we need to check if there exists any prev elems till now which were lesser than the current ele. Based on this we will store in a dp list.
When we traverse the prev elems, if it is smaller than the current ele what do we get.

The dp of the prev ele index i.e dp[j] has the value of the LIS till the jth ele. So for the current ele we will get the LIS as 1+dp[j]. Now we need to check for all the prev ele and each can have its own LIS. So max(dp[i], 1+dp[j]).

`Max check` was missed in prac => consider this going forward

`Prac 2 thought process`
------------------------------
In case of memozation its not a 1D dp but instead we will need a 2D dp to correctly track the changes. We also need a prev index which would help us to know what combo of indexes have been considered till now. Suppose index 4 would have been considered with index 1 and now it is also smaller than index 2 then these are 2 different cases.
Better to go with tabulation in this case => that looks like a simpler approach
