# LIS:

[Problem Link](https://leetcode.com/problems/longest-increasing-subsequence/description/)

`Prac 1 thought process`
------------------------------

This is the case of 1D dp. For each ele we need to check if there exists any prev elems till now which were lesser than the current ele. Based on this we will store in a dp list.
When we traverse the prev elems, if it is smaller than the current ele what do we get.

The dp of the prev ele index i.e dp[j] has the value of the LIS till the jth ele. So for the current ele we will get the LIS as 1+dp[j]. Now we need to check for all the prev ele and each can have its own LIS. So max(dp[i], 1+dp[j]).

`Max check` was missed in prac => consider this going forward