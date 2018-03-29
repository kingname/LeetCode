"""
https://leetcode.com/submissions/detail/147528781/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.




Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def insert(node, val_list):
            if not val_list:
                return

            middle_index = len(val_list) // 2
            middle = val_list[middle_index]
            if middle < node.val:
                node.left = TreeNode(middle)
                insert(node.left, val_list[:middle_index])
                insert(node.left, val_list[middle_index + 1: ])
            else:
                node.right = TreeNode(middle)
                insert(node.right, val_list[middle_index + 1: ])
                insert(node.right, val_list[: middle_index])

        if not nums:
            return None
        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])
        insert(root, nums[:middle_index])
        insert(root, nums[middle_index + 1:])
        return root
        