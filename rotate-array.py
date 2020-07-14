"""
https://leetcode.com/submissions/detail/300468465/

Given an array, rotate the array to the right by k steps, where&nbsp;k&nbsp;is non-negative.

Follow up:


	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
	Could you do it in-place with O(1) extra space?


&nbsp;
Example 1:


Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:


Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 2 * 10^4
	It&#39;s guaranteed that nums[i] fits in a 32 bit-signed integer.
	k &gt;= 0

"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            num = nums.pop(-1)
            nums.insert(0, num)