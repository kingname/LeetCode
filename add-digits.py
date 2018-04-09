"""
https://leetcode.com/submissions/detail/149194316/


Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 



For example:


Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


Follow up:
Could you do it without any loop/recursion in O(1) runtime?


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases."""


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 <= num <= 9:
            return num
        new_num = 0
        for n in str(num):
            new_num += int(n)
        return self.addDigits(new_num)
        