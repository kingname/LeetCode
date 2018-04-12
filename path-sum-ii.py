"""
https://leetcode.com/submissions/detail/149672048/


Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.


For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1



return

[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        self.walk(root, [], result, target)
        return result

    def walk(self, node, node_sum, result, target):
        node_sum.append(node.val)
        left = node.left
        right = node.right
        if not any([left, right]):
            if sum(node_sum) == target:
                result.append(node_sum)

        if left:
            self.walk(left, node_sum.copy(), result, target)
        if right:
            self.walk(right, node_sum.copy(), result, target)

       