"""
https://leetcode.com/submissions/detail/151539751/

Given an integer array nums, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.

Example:


Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation:&nbsp;[4,-1,2,1] has the largest sum = 6.


Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current = max_sum = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            max_sum = max(max_sum, current)
        return max_sum
            
        