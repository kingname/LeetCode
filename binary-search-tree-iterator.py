"""
https://leetcode.com/submissions/detail/370986912/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

&nbsp;




Example:




BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


&nbsp;

Note:


	next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
	You may assume that&nbsp;next()&nbsp;call&nbsp;will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        from collections import deque
        self.root = root
        self.stop = False
        self.iterator = self.do_iter(self.root)
        self.next_val = deque()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.next_val:
            return self.next_val.popleft()
        
        return self.try_to_get_next_val()

    def do_iter(self, node):
        if not node:
            return
        if node.left:
            yield from self.do_iter(node.left)
        yield node.val
        if node.right:
            yield from self.do_iter(node.right)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        next_val = self.try_to_get_next_val()
        if next_val is not None:
            self.next_val.append(next_val)
            return True
        else:
            return False

    def try_to_get_next_val(self):
        try:
            value = next(self.iterator)
            return value
        except StopIteration:
            return None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()