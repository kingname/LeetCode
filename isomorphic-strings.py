"""
https://leetcode.com/submissions/detail/149345916/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length."""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index_dict_s = {}
        index_dict_t = {}
        for index, letter in enumerate(zip(s, t)):
            if letter[0] in index_dict_s:
                index_dict_s[letter[0]].append(index)
            else:
                index_dict_s[letter[0]] = [index]
            if letter[1] in index_dict_t:
                index_dict_t[letter[1]].append(index)
            else:
                index_dict_t[letter[1]] = [index]

        for i in range(len(s)):
            x = index_dict_s[s[i]]
            y = index_dict_t[t[i]]
            if x != y:
                return False   

        return True