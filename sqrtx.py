"""
https://leetcode.com/submissions/detail/132357214/

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.



Example 1:

Input: 4
Output: 2



Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        return int(math.sqrt(x))
        