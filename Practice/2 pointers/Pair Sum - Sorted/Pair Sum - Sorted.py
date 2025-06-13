from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    n = len(nums)
    i, j = 0, n - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1

    return []
