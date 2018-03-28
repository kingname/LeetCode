"""
https://leetcode.com/submissions/detail/147352422/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3]  is not:

    1
   / \
  2   2
   \   \
   3    3




Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            if not left_node or not right_node:
                return False
            return left_node.val == right_node.val and is_mirror(left_node.left, right_node.right) and is_mirror(left_node.right, right_node.left)


        if not root:
            return True
        return is_mirror(root.left, root.right)