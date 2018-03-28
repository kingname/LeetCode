"""
https://leetcode.com/submissions/detail/147334825/

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list."""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        x = [str(k) for k in digits]
        digits_str = ''.join(x)
        digits_int = int(digits_str) + 1
        digits_str = str(digits_int)
        
        k = list(digits_str)
        return [int(m) for m in k]
        
        