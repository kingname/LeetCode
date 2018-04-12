"""
https://leetcode.com/submissions/detail/149683420/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1-&gt;2-&gt;3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,


    1
   / \
  2   3


&nbsp;

The root-to-leaf path 1-&gt;2 represents the number 12.
The root-to-leaf path 1-&gt;3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        all_path = []
        self.walk(root, [], all_path)
        s = 0
        for path in all_path:
            num = int(''.join(path))
            s += num
        return s

    def walk(self, node, current, result):
        current.append(str(node.val))
        left = node.left
        right = node.right
        if not left and not right:
            result.append(current)
        if left:
            self.walk(left, current.copy(), result)
        if right:
            self.walk(right, current.copy(), result)

        