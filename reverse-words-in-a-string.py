"""
https://leetcode.com/submissions/detail/20786527/


Given an input string, reverse the string word by word.



For example,
Given s = "the sky is blue",
return "blue is sky the".



Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.


click to show clarification.

Clarification:



What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.


"""


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = (' ').join(x for x in s.split())
        a = s.split(' ')
        thelen = len(a)
        b = ''
        for i in range(thelen):
            b +=a[-1*(i+1)]
            if i != thelen -1:
                b += ' ' 
        return b
        
        