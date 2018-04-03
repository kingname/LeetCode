"""
https://leetcode.com/submissions/detail/148251692/

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p1 = head
        p2 = head.next
        p1.next = None
        while True:
            if not p2:
                return p1
            if not p2.next:
                p2.next = p1
                return p2
            p3 = p2.next
            p2.next = p1
            if p1 is head:
                p1.next = None
            p1 = p2
            p2 = p3
                

        
        