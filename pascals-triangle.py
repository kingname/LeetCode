"""
https://leetcode.com/submissions/detail/147660185/

Given numRows, generate the first numRows of Pascal's triangle.


For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = []
            for upper in range(i + 1):
                if upper in [0, i]:
                    row.append(1)
                else:
                    row.append(result[-1][upper - 1] + result[-1][upper])
            result.append(row)
        return result
            
        