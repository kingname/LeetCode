"""
https://leetcode.com/submissions/detail/149681469/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.walk([root], result)
        return result

    def walk(self, node_list, result):
        lower_level_node_list = []
        this_level = []
        for node in node_list:
            this_level.append(node.val)
            left = node.left
            right = node.right
            
            if left:
                lower_level_node_list.append(left)
            if right:
                lower_level_node_list.append(right)
        result.append(this_level)
        if lower_level_node_list:
            self.walk(lower_level_node_list, result)
            
        