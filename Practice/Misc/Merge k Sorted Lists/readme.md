# Merge k Sorted Lists

[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)

## Problem Statement

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

`Prac 1`:

Tried a brute force approach where traversed all the lists till they have any element present.
At each step which linked list had the smallest value => based on that updated the answer and updated that head to head.next
O(n\*k) solution => can pass test cases but needs to be optimized.

2 ways to optimize:

> Using Min Heap
> We can store the head of the linked list in a min heap => this way we will get the min value every time we pop and we can push the next in the min heap

> Using divide and conquer
> Same approach as merge sort => only thing here is we will have a method which gives us 2 lists l1 and l2 and then another method which would create a sorted list based on the input lists. Pattern can be used in other places as well.

> Both solution will be O(n log k)

---

N = total number of nodes across all lists.
log k time to maintain the heap of size k.

N: total number of nodes in all lists.
log k: because the list is divided in log k levels.
At each level, we merge all nodes once across pairs → total work = O(N log k)
