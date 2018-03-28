"""
https://leetcode.com/submissions/detail/147348992/

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
        if not root:
            return True
        new_lower_level = []
        lower_level = [root]
        count = 1
        while True:
            level_val = [None] * (2 ** count)
            count += 1
            for index, x in enumerate(lower_level):
                level_val[index * 2] = x.left.val if x and x.left else None
                level_val[index * 2 + 1] = x.right.val if x and x.right else None
            if level_val != level_val[::-1]:
                return False

            for level in lower_level:
                new_lower_level.append(level.left if level else None)
                new_lower_level.append(level.right if level else None)

            if not any(new_lower_level):
                return True
            lower_level = new_lower_level.copy()
            new_lower_level = []