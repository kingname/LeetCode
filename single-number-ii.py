"""
https://leetcode.com/submissions/detail/149527154/


Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.



Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        unique_sum = sum(set(nums))
        other = (total_sum - unique_sum) / 2
        
        return int(unique_sum - other)
        