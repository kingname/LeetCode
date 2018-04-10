"""
https://leetcode.com/submissions/detail/149357269/


Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.



According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”



        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5



For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        target_dict = {'p': p, 'q': q}

        def walk(node, parent, path_list):
            parent.append(node)
            if node is p:
                target_dict.pop('p')
                path_list.append(parent)
            if node is q:
                target_dict.pop('q')
                path_list.append(parent)

            if not target_dict:
                return

            left = node.left
            right = node.right
            if left:
                walk(left, [x for x in parent], path_list)
            if right:
                walk(right, [x for x in parent], path_list)
        path_list = []
        walk(root, [], path_list)
        short_one, long_one = sorted(path_list, key=lambda x: len(x))
        if short_one[-1] in long_one:
            return short_one[-1]

        upper = None
        for node_tuple in zip(short_one, long_one):
            if node_tuple[0] == node_tuple[1]:
                upper = node_tuple[0]
            else:
                return upper
        
        