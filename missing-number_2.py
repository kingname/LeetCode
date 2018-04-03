"""
https://leetcode.com/submissions/detail/148301162/


Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.


Example 1

Input: [3,0,1]
Output: 2



Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8





Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases."""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_nums = set([x for x in range(len(nums) + 1)])
        lost_num = right_nums - set(nums)
        return lost_num.pop()