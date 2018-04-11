"""
https://leetcode.com/submissions/detail/149525102/

Write a function that takes a string as input and reverse only the vowels of a string.


Example 1:
Given s = "hello", return "holle".



Example 2:
Given s = "leetcode", return "leotcede".



Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_list = 'aeiouAEIOU'
        result = ''
        vowel_letter_list = []
        for letter in s:
            if letter not in vowel_list:
                result += letter
            else:
                result += '{}'
                vowel_letter_list.append(letter)
        print(result, vowel_letter_list)
        return result.format(*(vowel_letter_list[::-1]))
