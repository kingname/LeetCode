"""
https://leetcode.com/submissions/detail/149199495/

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5


Credits:Special thanks to @mithmatt for adding this problem and creating all test cases."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        point = head
        parent = None
        while point:
            if point.val == val:
                if parent is None:
                    head = head.next
                point = point.next
                continue
            if parent is None:
                parent = point
            else:
                parent.next = point
                parent = point
            point = point.next

        if parent:
            parent.next = None
        return head

        