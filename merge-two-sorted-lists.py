"""
https://leetcode.com/submissions/detail/84887504/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        full_dict = {}
        if l1:
            for each in self.ite(l1):
                if each.val not in full_dict:
                    full_dict[each.val] = [each]
                else:
                    full_dict[each.val].append(each)
        if l2:
            for each in self.ite(l2):
                if each.val not in full_dict:
                    full_dict[each.val] = [each]
                else:
                    full_dict[each.val].append(each)
        item_list = sorted(full_dict.items(), key=lambda x: x[0])
        node_list = [x[1] for x in item_list]
        node_list = [x for y in node_list for x in y]
        print(node_list)
        return self.comb(node_list) if node_list else None

    def ite(self, node):
        node_list = []
        while node.next:
            node_list.append(node)
            node = node.next
        node_list.append(node)
        return node_list

    def comb(self, node_list):
        print(len(node_list))
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[-1].next = None
        return node_list[0]
            
        