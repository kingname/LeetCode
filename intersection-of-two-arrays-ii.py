"""
https://leetcode.com/submissions/detail/149376651/


Given two arrays, write a function to compute their intersection.


Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].


Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.



Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_list = [nums1, nums2]
        short_list, long_list = sorted(num_list, key=lambda x: len(x))

        result = []
        for num in short_list:
            if num in long_list:
                result.append(num)
                long_list.pop(long_list.index(num))
        return result
        