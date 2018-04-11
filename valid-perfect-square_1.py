"""
https://leetcode.com/submissions/detail/149522619/

Given a positive integer num, write a function which returns True if num is a perfect square else False.


Note: Do not use any built-in library function such as sqrt.


Example 1:

Input: 16
Returns: True



Example 2:

Input: 14
Returns: False



Credits:Special thanks to @elmirap for adding this problem and creating all test cases."""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        for i in range(1, num // 2 + 1):
            if i ** 2 == num:
                return True
            elif i ** 2 > num:
                return False
        return False
        