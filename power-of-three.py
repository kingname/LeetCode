"""
https://leetcode.com/submissions/detail/149375567/


    Given an integer, write a function to determine if it is a power of three.


    Follow up:
    Could you do it without using any loop / recursion?


Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases."""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n / 3
        return True
        