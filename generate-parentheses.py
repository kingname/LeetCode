"""
https://leetcode.com/submissions/detail/151684602/


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



For example, given n = 3, a solution set is:


[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        all_result = []
        queue = [(['('] * n, [')'] * n, 0, '')]
        while queue:
            task = queue.pop(0)
            left = task[0]
            right = task[1]
            uncomplete_left_num = task[2]
            current_result = task[3]
            if uncomplete_left_num <= 0 and left:
                current_result += left.pop(0)
                uncomplete_left_num += 1
                queue.append((left, right, uncomplete_left_num, current_result))
            else:
                # option 1: still left
                if left:
                    n_left = left.copy()
                    n_current = current_result
                    n_current += n_left.pop(0)
                    n_uncomplete_left = uncomplete_left_num
                    n_uncomplete_left += 1
                    queue.append((n_left, right, n_uncomplete_left, n_current))
                # option 2: right
                n_right = right.copy()
                current_result += n_right.pop(0)
                uncomplete_left_num -= 1
                if n_right:
                    queue.append((left, n_right, uncomplete_left_num, current_result))
                else:
                    all_result.append(current_result)
        return all_result

        
            
            
        