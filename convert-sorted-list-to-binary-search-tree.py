"""
https://leetcode.com/submissions/detail/150250407/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.




Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        number_list = []
        while head:
            number_list.append(head.val)
            head = head.next
        root = self.generate(number_list)
        return root

    def generate(self, number_list):
        if len(number_list) == 1:
            return TreeNode(number_list[0])
        if len(number_list) == 2:
            root = TreeNode(number_list[0])
            root.right = TreeNode(number_list[1])
            return root
        mid = len(number_list) // 2
        root = TreeNode(number_list[mid])
        left_group = number_list[:mid]
        right_group = number_list[mid + 1: ]
        if len(left_group) == 1:
            root.left = TreeNode(left_group[0])
        else:
            root.left = self.generate(left_group)
        if len(right_group) == 1:
            root.right = TreeNode(right_group[0])
        else:
            root.right = self.generate(right_group)
        return root
        