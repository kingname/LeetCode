"""
https://leetcode.com/submissions/detail/149375985/


Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true.
Given num = 5, return false.


Follow up: Could you solve it without loops/recursion?

Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases."""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num <= 0 or num == 2:
            return False
        power =  math.log(num) / math.log(4) 
        if int(power) == power:
            return True
        return False
        