"""
https://leetcode.com/submissions/detail/366981662/

Given a singly linked list L: L0&rarr;L1&rarr;&hellip;&rarr;Ln-1&rarr;Ln,
reorder it to: L0&rarr;Ln&rarr;L1&rarr;Ln-1&rarr;L2&rarr;Ln-2&rarr;&hellip;

You may not modify the values in the list&#39;s nodes, only nodes itself may be changed.

Example 1:


Given 1-&gt;2-&gt;3-&gt;4, reorder it to 1-&gt;4-&gt;2-&gt;3.

Example 2:


Given 1-&gt;2-&gt;3-&gt;4-&gt;5, reorder it to 1-&gt;5-&gt;2-&gt;4-&gt;3.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        point = head
        node_list = []
        while point:
            node_list.append(point)
            point = point.next
            
        point = head
        for node in node_list[::-1]:
            if point is node:
                point.next = None
                break
            next_origin = point.next
            if next_origin is node:
                node.next = None
                break
            node.next = next_origin
            point.next = node
            point = next_origin
            