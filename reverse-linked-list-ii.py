"""
https://leetcode.com/submissions/detail/369204158/

Reverse a linked list from position m to n. Do it in one-pass.

Note:&nbsp;1 &le; m &le; n &le; length of list.

Example:


Input: 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL, m = 2, n = 4
Output: 1-&gt;4-&gt;3-&gt;2-&gt;5-&gt;NULL

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        parent = None
        p1 = head
        start = p1
        node_count = 1
        while node_count < m:
            parent = p1
            p1 = p1.next
            start = p1
            node_count += 1

        p2 = p1.next
        p3 = p2.next
        while node_count < n:
            p2.next = p1
            p1 = p2
            p2 = p3
            node_count += 1
            if p3:
                p3 = p3.next

        start.next = p2
        if parent:
            parent.next = p1
        else:
            head = p1
        return head
        
