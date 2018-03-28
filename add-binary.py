"""
https://leetcode.com/submissions/detail/132357011/


Given two binary strings, return their sum (also a binary string).



For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = int(a, 2)
        b_int = int(b, 2)
        result = a_int + b_int
        return '{0:b}'.format(result)
        