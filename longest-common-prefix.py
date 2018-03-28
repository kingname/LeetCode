"""
https://leetcode.com/submissions/detail/132286213/

Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        others = strs[1:]
        prefix = ''
        for letter in first:
            prefix += letter
            for other in others:
                if not other.startswith(prefix):
                    return prefix[:-1]
        return prefix
                
                        
        