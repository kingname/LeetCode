"""
https://leetcode.com/submissions/detail/149523727/

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
        count = 1
        x = num
        last_x = num
        while True:
            x = x - x / 2 + num / 2 / x
            if last_x == int(x):
                return False
            if int(x) ** 2 == num:
                return True
            count += 1
            last_x = int(x)
        