"""
https://leetcode.com/submissions/detail/132355791/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2



Example 2:

Input: [1,3,5,6], 2
Output: 1



Example 3:

Input: [1,3,5,6], 7
Output: 4



Example 1:

Input: [1,3,5,6], 0
Output: 0

"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target in nums:
            return nums.index(target)
        for index, num in enumerate(nums):
            if num > target:
                return index
        return len(nums)
        