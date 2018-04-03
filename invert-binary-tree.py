"""
https://leetcode.com/submissions/detail/148302980/

Invert a binary tree.


     4
   /   \
  2     7
 / \   / \
1   3 6   9

to


     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can&rsquo;t invert a binary tree on a whiteboard so f*** off.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            invert(node.left) 
            invert(node.right)
        invert(root)
        return root