"""
https://leetcode.com/submissions/detail/149670707/

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] &ne; num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -&infin;.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.


Credits:Special thanks to @ts for adding this problem and creating all test cases."""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0

        if nums[0] > nums[1]:
            return 0

        for index, num in enumerate(nums):
            if index >0 and index < len(nums) - 1:
                if nums[index - 1] < num and num > nums[index + 1]:
                    return index
        return index