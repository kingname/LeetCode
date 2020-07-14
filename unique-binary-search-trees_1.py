"""
https://leetcode.com/submissions/detail/366544583/

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
        def count(num_list):
            if len(num_list) <= 1:
                return 1
            if len(num_list) == 2:
                return 2
            tree_count = 0
            for index, root_node in enumerate(num_list):
                tree_count += count(num_list[: index]) * count(num_list[index + 1:])
            return tree_count
        full_num_list = tuple(range(1, n + 1))
        if n <= 2:
            return count(full_num_list)
        tree_count = count(full_num_list)
        return tree_count 
        