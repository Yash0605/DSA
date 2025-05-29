class Solution:

    def subsetHelper(self, nums, target, index):
        # base case
        if target == 0:
            return 1
        if index == len(nums) or target < 0:
            return 0

        # pick
        pick = 0
        if target - nums[index] >= 0:
            pick = self.subsetHelper(nums, target - nums[index], index + 1)

        # dont pick the element
        dont_pick = self.subsetHelper(nums, target, index + 1)

        return pick + dont_pick

    def helper(self, nums, target, current_sum, index, dp):
        # base case
        if index == len(nums):
            return current_sum == target

        if (index, current_sum) in dp:
            return dp[(index, current_sum)]
        ans = 0

        # - operator
        ans += self.helper(nums, target, current_sum - nums[index], index + 1, dp)

        # + operator
        ans += self.helper(nums, target, current_sum + nums[index], index + 1, dp)

        dp[(index, current_sum)] = ans
        return dp[(index, current_sum)]

    """
    Tabulation approach for subset
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total = sum(nums)

        # edge case
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        required_target = (total + target) // 2

        dp = [[0] * (required_target + 1) for _ in range(n + 1)]

        dp[0][0] = 1  # we can always get the taget as 0 if we dont pick any element

        # first row will be 0 appart from 0,0 because we cannot achieve any target>1 with 0 element

        # first col will always be 1 as we can achieve target = 0 if we don't pick any element => only tru if nums do not have 0
        # for i in range(1,n+1):
        #     dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(required_target + 1):
                # don't pick the ele
                dp[i][j] = dp[i - 1][j]

                # pick the ele => only possible if target is greater than or equal to element
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[n][required_target]

    """
    Using Maths and subset
    We know that some ele can have +ve operator and some can have -ve operator
    So nums can be divided in 2 subsets
        - P => has all the ele with positive values
        - N => has all the ele with negative 
        P+N = total
        P-N = target -. as per the problem
        Eg:[1,1,1,1,1] => P = ele at [0,2,3,4] 
                        => N = ele at [1]
                        => if target = 3 => then can be achieved by P-N

        P+N = total
        P-N = target
        2P = total+target
        P = (total+target)/2
        Thus this comes down to finding how many such subsets exists
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        # need to use dictionary rather than list beacuse current sum can have -ve values and we cannot have -ve indexes
        total = sum(nums)

        # edge case
        if abs(target) > total:
            return 0

        if (total + target) % 2 != 0:
            return 0

        required_target = (total + target) // 2

        count_zeroes = nums.count(0)
        non_zero_nums = [num for num in nums if num != 0]

        val = self.subsetHelper(non_zero_nums, required_target, 0)

        print(val)

        return val*(2**count_zeroes)
    """

    """
    Tabulation - using problem statement
    

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        # need to use dictionary rather than list beacuse current sum can have -ve values and we cannot have -ve indexes
        total = sum(nums)

        # edge case
        if abs(target) > total:
            return 0

        dp = [[0] * (2 * total + 1) for _ in range(n)]

        # initial conditions
        dp[0][total + nums[0]] = 1
        dp[0][total - nums[0]] += 1

        for i in range(1, n):
            for j in range(0, 2 * total + 1):
                if dp[i - 1][j] > 0:
                    dp[i][j + nums[i]] += dp[i - 1][j]
                    dp[i][j - nums[i]] += dp[i - 1][j]

        return dp[n - 1][target+total]

    """

    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # return self.helper(nums, target, 0, 0)

        # Memoization
        n = len(nums)
        # need to use dictionary rather than list beacuse current sum can have -ve values and we cannot have -ve indexes
        dp = {}
        return self.helper(nums, target, 0, 0, dp)
    """
