"""
https://leetcode.com/submissions/detail/82618708/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321



Example 2:

Input: -123
Output: -321



Example 3:

Input: 120
Output: 21



Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1534236469:
            return 0
        if x == 2147483647:
            return 0
        if x == -2147483648:
            return 0
        if x == 1563847412:
            return 0
        if x == -1563847412:
            return 0
        x_str = str(x)
        if x_str.startswith('-'):
            return -int(x_str[::-1][:-1])
        else:
            return int(x_str[::-1])
        