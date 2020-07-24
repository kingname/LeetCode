"""
https://leetcode.com/submissions/detail/369690505/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:


Input: 4-&gt;2-&gt;1-&gt;3
Output: 1-&gt;2-&gt;3-&gt;4


Example 2:


Input: -1-&gt;5-&gt;3-&gt;4-&gt;0
Output: -1-&gt;0-&gt;3-&gt;4-&gt;5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, node1, node2):
        temp_node = temp_node_head = ListNode(0)
        while node1 and node2:
            if node1.val < node2.val:
                temp_node_head.next = node1
                node1 = node1.next
            else:
                temp_node_head.next = node2
                node2 = node2.next
            temp_node_head = temp_node_head.next
        temp_node_head.next = node1 or node2
        temp_node = temp_node.next
        return temp_node
            

    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        node_list_2_head = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(node_list_2_head)
        return self.merge(left, right)

        
        
            
        
                        
                
        
            
            