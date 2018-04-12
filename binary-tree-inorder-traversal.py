"""
https://leetcode.com/submissions/detail/149679020/

Given a binary tree, return the inorder traversal of its nodes' values.


For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3



return [1,3,2].


Note: Recursive solution is trivial, could you do it iteratively?"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        self.walk(root, result)
        return result

    def walk(self, node, result):
        left = node.left
        right = node.right
        if not left and not right:
            result.append(node.val)
            return

        if left:
            self.walk(left, result)
        result.append(node.val)
        if right:
            self.walk(right, result)
        
        