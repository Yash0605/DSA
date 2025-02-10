class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]

        curr_sum, max_sum = 0, nums[0]

        for num in nums:
            curr_sum+=num

            if curr_sum > max_sum:
                max_sum = curr_sum
            
            if curr_sum<0:
                curr_sum = 0

        return max_sum
        