"""
https://leetcode.com/submissions/detail/132367965/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],


    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_all_path(root_node, all_path, current_path):
            current_path += ',{}'.format(root_node.val)
            if root_node.left:
                get_all_path(root_node.left, all_path, current_path)
            else:
                all_path.append(current_path)
            if root_node.right:
                get_all_path(root_node.right, all_path, current_path)
            else:
                all_path.append(current_path)

        if not root:
            return 0
        up_node = None
        all_path_list = []
        get_all_path(root, all_path_list, '')
        length = 0
        for path in all_path_list:
            path = path.strip(',').split(',')
            if len(path) > length:
                length = len(path)
        return length
        
        