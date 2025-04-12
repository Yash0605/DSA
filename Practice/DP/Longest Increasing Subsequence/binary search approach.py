class Solution:
    import bisect
    from typing import List

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        sub = []

        for num in nums:
            """
            sub:
            Stores the smallest possible tail of an increasing subsequence of each length.
            It doesn't store the actual LIS, but its length is the correct answer.

            We're finding the first index in arr where target can be inserted without breaking the order.
            If all elements are smaller than target, it returns len(arr) (meaning target should be appended).
            If target exists in arr, it returns the index of the first occurrence.
            lower bound implementation
            """
            index = bisect.bisect_left(sub, num)

            if index == len(sub):
                sub.append(num)
            else:
                sub[index] = num

        return len(sub)
