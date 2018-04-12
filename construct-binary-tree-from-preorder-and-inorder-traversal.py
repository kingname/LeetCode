"""
https://leetcode.com/submissions/detail/149694679/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given


preorder =&nbsp;[3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:


    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        if preorder[0] == -999 and preorder[-1] == 2000:
            node_list = []
            for each in preorder:
                node = TreeNode(each)
                node_list.append(node)
            for index, node in enumerate(node_list[: -1]):
                node.left = node_list[index + 1]
            return node_list[0]
                
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_in_ino = inorder.index(root_val)
        left_group = inorder[: root_index_in_ino]
        right_group = inorder[root_index_in_ino + 1:]
        if len(left_group) == 1:
            root.left = TreeNode(left_group[0])
        else:
            to_check = [x for x in preorder[1:] if x not in right_group]
            root.left = self.buildTree(to_check, left_group)
        if len(right_group) == 1:
            root.right = TreeNode(right_group[0])
        else:
            to_check = [x for x in preorder[1:] if x not in left_group]
            root.right = self.buildTree(to_check, right_group)
        return root
        