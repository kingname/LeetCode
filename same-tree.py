"""
https://leetcode.com/submissions/detail/132364484/


Given two binary trees, write a function to check if they are the same or not.


Two binary trees are considered the same if they are structurally identical and the nodes have the same value.




Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true



Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false



Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def walk(root, val_list):
            val_list.append(root.val)
            if root.left:
                walk(root.left, val_list)
            else:
                val_list.append(None)
            if root.right:
                walk(root.right, val_list)
            else:
                val_list.append(None)

        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False
        
        p_list = []
        q_list = []
        walk(p, p_list)
        walk(q, q_list)
        return p_list == q_list
        