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

Binary search can also be used but its not a straight forward solution.

import java.util.*;

class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> sub = new ArrayList<>();

        for (int num : nums) {
            int i = Collections.binarySearch(sub, num);

            if (i < 0) {
                i = -(i + 1);  // index to insert
            }

            if (i == sub.size()) {
                sub.add(num);
            } else {
                sub.set(i, num);
            }
        }

        return sub.size();
    }
}

Step-by-Step Explanation:
🔸 for (int num : nums)
Iterates over every number in the input array nums.

🔸 int i = Collections.binarySearch(sub, num);
We do a binary search in the sub list to find where num fits.

If num is already in sub, it returns the index.

If not, it returns -(insertion_point + 1) — a negative value.

🔸 if (i < 0) { i = -(i + 1); }
This converts the negative return value to the actual insertion point.

So now i tells us where num should be placed (or replaced) in sub.

🔸 if (i == sub.size())
If num is greater than every element in sub, i will be equal to the size of sub.

That means we're extending the LIS, so we append num.

🔸 else { sub.set(i, num); }
If num can replace an element in sub to maintain a smaller ending value at that position, we do it.

This keeps sub optimized for future insertions (smaller tails = more flexibility).
