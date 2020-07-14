"""
https://leetcode.com/submissions/detail/366551160/

Given n, how many structurally unique BST&#39;s (binary search trees) that store values 1 ...&nbsp;n?

Example:


Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST&#39;s:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution:
    def numTrees(self, n: int) -> int:
        
        from functools import lru_cache
        
        @lru_cache
        def count(num):
            if num <= 1:
                return 1
            if num == 2:
                return 2
            tree_count = 0
            for i in range(num):
                tree_count += count(i) * count(num - i - 1)
            return tree_count
        tree_count = count(n)
        return tree_count 
        