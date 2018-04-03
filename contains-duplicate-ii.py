"""
https://leetcode.com/submissions/detail/148298578/


Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        
        index_dict = {}
        for index, num in enumerate(nums):
            if num not in index_dict:
                index_dict[num] = index
            else:
                pre_index = index_dict[num]
                if abs(index - pre_index) <= k:
                    return True
                else:
                    index_dict[num] = index
        return False