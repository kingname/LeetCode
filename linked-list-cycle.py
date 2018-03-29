"""
https://leetcode.com/submissions/detail/147499307/


Given a linked list, determine if it has a cycle in it.



Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False


        point_1 = head
        point_2 = head.next
        while True:
            if not point_1 or not point_2:
                return False
            point_1 = point_1.next
            point_2 = point_2.next
            if point_2 == point_1:
                return True
            if point_2:
                point_2 = point_2.next
                if point_2 == point_1:
                    return True
        