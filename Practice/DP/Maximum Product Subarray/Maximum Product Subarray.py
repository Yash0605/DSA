# DP way
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Base logic is that if a big number is multiplied with a neg number then ans is a smaller number => pos * neg
        if a smaller number is multiplied with a neg number then ans is a bigger number => neg * neg
        We will maintain 2 variables currentMin and currentMax
        3 cases => no 0 and odd neg
                => no 0 and pos neg => same as all pos
                => has 0 => then ans would be some subarray
        how to deal with 0 => skip ?
        """
        ans, currentMax, currentMin = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            # swap the values of currentMax and currentMin if the current number is negative
            # this is because multiplying a negative number with the current minimum will give us the maximum product
            if nums[i] < 0:
                currentMax, currentMin = currentMin, currentMax

            # case for 0 => if 0 found then next element would essentialy be max or min
            # => resetting the value

            currentMax = max(nums[i], currentMax * nums[i])
            currentMin = min(nums[i], currentMin * nums[i])

            ans = max(ans, currentMax)

        return ans


# Way 2
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre, suff = 1, 1
        max_product = float("-inf")

        if n == 1 and nums[0] == 0:
            return 0

        for i in range(n):
            # if pre == 0:
            #     pre=1
            # if suff == 0:
            #     suff=1

            #  short circuiting the multiplication if pre or suff is 0
            # this is a bit tricky, but it works because if pre or suff is 0, we don't want to multiply by 0
            pre = (pre or 1) * nums[i]
            suff = (suff or 1) * nums[n - i - 1]

            max_product = max(max_product, pre, suff)

        return max(max_product, pre, suff)
