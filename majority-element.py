"""
https://leetcode.com/submissions/detail/147500469/

Given an array of size n, find the majority element. The majority element is the element that appears more than &lfloor; n/2 &rfloor; times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:Special thanks to @ts for adding this problem and creating all test cases."""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for each in nums:
            if each in freq:
                freq[each] += 1
            else:
                freq[each] = 1
        
        result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return result[0][0]
        