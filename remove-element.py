"""
https://leetcode.com/submissions/detail/132347723/

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn&#39;t matter what you leave beyond the new length.

Example:


Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.


&nbsp;
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            index = nums.index(val)
            nums.pop(index)
        return len(nums)
            
        