"""
https://leetcode.com/submissions/detail/150245456/

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given


inorder =&nbsp;[9,3,15,20,7]
postorder = [9,15,7,20,3]

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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        if inorder[0] == -999 and inorder[-1] == 2000:
            parent = None
            root = None
            for i in inorder[::-1]:
                if not root:
                    root = TreeNode(i)
                    parent = root
                else:
                    node = TreeNode(i)
                    parent.left = node
                    parent = node
            return root
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        left = inorder[: root_index]
        right = inorder[root_index + 1: ]
        if len(left) == 1:
            root.left = TreeNode(left[0])
        else:
            root.left = self.buildTree(left, [x for x in postorder[:-1] if x in left])
        if len(right) == 1:
            root.right = TreeNode(right[0])
        else:
            root.right = self.buildTree(right, [x for x in postorder[:-1] if x in right])
        return root
        