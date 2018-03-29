"""
https://leetcode.com/submissions/detail/147517696/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def get_leaf(node_list, result):
            new_node_list = []
            value_list = []
            if not any(node_list):
                return
            for node in node_list:
                if node:
                    value_list.append(node.val)
                    new_node_list.append(node.left)
                    new_node_list.append(node.right)
            result.append(value_list)
            get_leaf(new_node_list, result)

        if not root:
            return []
        
        result = []
        get_leaf([root], result)
        return result[::-1]
        
        