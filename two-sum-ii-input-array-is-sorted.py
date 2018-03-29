"""
https://leetcode.com/submissions/detail/147485769/

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.


Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        nums = []
        for index, num in enumerate(numbers):
            if num in index_dict:
                index_dict[num][1] += 1
            else:
                index_dict[num] = [index, 1]
            nums.append(num)
        for num in nums:
            another = target - num
            if num != another and another in index_dict:
                return [index_dict[num][0] + 1, index_dict[another][0] + 1]
            if num == another and index_dict[another][1] > 1:
                return [index_dict[num][0] + 1, index_dict[num][0] + 2]
        