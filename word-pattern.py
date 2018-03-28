"""
https://leetcode.com/submissions/detail/132289433/

Given a pattern and a string str, find if str follows the same pattern.
 Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.




Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases."""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word = str.split(' ')
        pattern_list = list(pattern)
        
        if len(word) != len(pattern_list):
            return False
        
        pair_list = zip(pattern_list, word)
        pair_dict = {}
        for pair in pair_list:
            if pair[0] in pair_dict:
                pair_dict[pair[0]].append(pair[1])
            else:
                pair_dict[pair[0]] =  [pair[1]]
        comman_list = []
        for v in pair_dict.values():
            if len(set(v)) != 1:
                return False
            comman_list.append(v[0])
        if len(comman_list) != len(set(comman_list)):
            return False
        return True
        