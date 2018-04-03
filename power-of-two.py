"""
https://leetcode.com/submissions/detail/148299045/


Given an integer, write a function to determine if it is a power of two.


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases."""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        binary = '{0:b}'.format(n)
        start_flag = False
        for bit in binary:
            if bit == '1':
                if start_flag:
                    return False
                start_flag = True
        return True