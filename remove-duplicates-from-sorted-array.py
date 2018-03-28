"""
https://leetcode.com/submissions/detail/134254543/


Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        already = []
        for n in nums:
            if n not in already:
                already.append(n)
        for index, n in enumerate(already):
            nums[index] = n
        return len(already)
        