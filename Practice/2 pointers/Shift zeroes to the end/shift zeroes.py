from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0
