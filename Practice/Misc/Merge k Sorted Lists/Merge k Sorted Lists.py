# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        if lists and not lists[0] and len(lists) == 1:
            return None

        if lists and len(lists) == 1:
            return lists[0]

        # using divide and conquer
        """
        2 methods required
        => one sets the range of linked lists to be checked
        => another one compares 2 linked list and return the sorted linked list
        """

        def mergeRange(left, right):
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            l1 = mergeRange(left, mid)
            l2 = mergeRange(mid + 1, right)
            return mergeTwoLists(l1, l2)

        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
                current = current.next

            while l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
                current = current.next

            while l2:
                current.next = ListNode(l2.val)
                l2 = l2.next
                current = current.next

            return dummy.next

        return mergeRange(0, len(lists) - 1)

        """
        Brute Force
        ----------------------------

        answerHead = None
        finalAnswerhead = None
        hasMoreElements = True

        while hasMoreElements:
            isNextPresent = False
            currentMinVal = float("inf")
            minIndex = -1

            for i in range(len(lists)):
                if lists[i] and lists[i].val < currentMinVal:
                    currentMinVal = lists[i].val
                    minIndex = i

                if lists[i]:
                    isNextPresent = True

            # updating the head of the list which had the current minimum value
            if minIndex!=-1:
                lists[minIndex] = lists[minIndex].next

                if not answerHead:
                    answerHead = ListNode(currentMinVal)
                    finalAnswerhead = answerHead
                else:
                    answerHead.next = ListNode(currentMinVal)
                    answerHead = answerHead.next

            if not isNextPresent:
                hasMoreElements = False

        return finalAnswerhead

        """


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        """
        using min heap
        """
        if not lists:
            return None

        if lists and len(lists) == 1 and not lists[0]:
            return None

        minHeap = []
        currentIndex = count()
        answer = ListNode(0)
        current = answer

        for linkedList in lists:
            if linkedList:
                heapq.heappush(
                    minHeap, (linkedList.val, next(currentIndex), linkedList)
                )

        while minHeap:
            currentMinVal, _, currentNode = heapq.heappop(minHeap)

            if currentNode.next:
                heapq.heappush(
                    minHeap,
                    (currentNode.next.val, next(currentIndex), currentNode.next),
                )

            current.next = ListNode(currentMinVal)
            current = current.next

        return answer.next
