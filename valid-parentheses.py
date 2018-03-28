"""
https://leetcode.com/submissions/detail/132287314/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        quote_dict = {')': '(', ']': '[', '}': '{'}
        rebuild = ''
        for char in s:
            if char in ['(', '[', '{']:
                rebuild += char
            elif char in [')', ']', '}']:
                if rebuild and rebuild[-1] == quote_dict[char]:
                    rebuild = rebuild[:-1]
                else:
                    return False
        if not rebuild:
            return True
        return False

            
            
        