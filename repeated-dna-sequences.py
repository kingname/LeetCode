"""
https://leetcode.com/submissions/detail/149669061/


All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seq_dict = {}
        for start_index in range(len(s) - 9):
            seq = s[start_index: start_index + 10]
            if seq in seq_dict:
                seq_dict[seq] += 1
            else:
                seq_dict[seq] = 1
        return [key for key in seq_dict if seq_dict[key] >= 2]
        