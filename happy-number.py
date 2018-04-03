"""
https://leetcode.com/submissions/detail/148247793/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:&nbsp;19 is a happy number


12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Credits:Special thanks to @mithmatt and @ts for adding this problem and creating all test cases."""


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already = set()
        def check(num):
            if num in already:
                return False
            already.add(num)
            new_num = 0
            
            for letter in str(num):
                new_num += int(letter) ** 2
            if new_num == 1:
                return True
            return check(new_num)
        return check(n)