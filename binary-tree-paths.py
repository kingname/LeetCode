"""
https://leetcode.com/submissions/detail/149352334/


Given a binary tree, return all root-to-leaf paths.


For example, given the following binary tree:



   1
 /   \
2     3
 \
  5



All root-to-leaf paths are:
["1->2->5", "1->3"]


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases."""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        def walk(node, parent_list, path_list):
            left = node.left
            right = node.right
            parent_list.append(str(node.val))
            if not left and not right:
                path_list.append('->'.join(parent_list))
                return
            if left:
                walk(left, parent_list.copy(), path_list)
            if right:
                walk(right, parent_list.copy(), path_list)
        path_list = []
        walk(root, [], path_list)
        return path_list
        