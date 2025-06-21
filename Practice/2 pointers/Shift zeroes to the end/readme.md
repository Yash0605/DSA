# Shift Zeros to the End

[Shift Zeros to the End](https://bytebytego.com/exercises/coding-patterns/two-pointers/shift-zeros-to-the-end)

Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]

## Prac 1 thought process

This uses the two-pointer approach: i tracks the position for the next non-zero number, and j scans through the list.

if no zeroes then as per logic every ele will swap with itself i.e no changes and i keeps on incrementing
Once 0 found => j increments coz of loop but i is fixed at the pos so we are able to reach any index which has 0 and then stop there till we get a non zero ele

ANother option is to move all non zero ele to the front and then fill the list with zeroes