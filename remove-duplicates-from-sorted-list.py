"""
https://leetcode.com/submissions/detail/132361075/


Given a sorted linked list, delete all duplicates such that each element appear only once.


For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current_value = head.val
        current_node = head
        next_node = head.next
        while next_node:
            if next_node.val > current_node.val:
                current_node = next_node
                next_node = next_node.next
            else:
                next_node = next_node.next
                current_node.next = next_node
        return head