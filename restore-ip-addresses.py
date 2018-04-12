"""
https://leetcode.com/submissions/detail/149666836/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given &quot;25525511135&quot;,

return [&quot;255.255.11.135&quot;, &quot;255.255.111.35&quot;]. (Order does not matter)
"""


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        def split(st, n, ip, result):
            ip = ip.copy()
            if n > 1:
                for i in range(1, 4):
                    part = st[:i]
                    if part and 0 <= int(part) <= 255:
                        if len(part) > 1 and part.startswith('0'):
                            continue
                        ip.append(part)
                        split(st[i:], n - 1, ip.copy(), result)
                        ip.pop(-1)
            else:
                flag = False
                for i in range(1, 4):
                    part_3, part_4 = st[:i], st[i:]
                    if part_3 and part_4 and 0 <= int(part_3) <= 255 and 0 <= int(part_4) <= 255:
                        if len(part_3) > 1 and part_3.startswith('0'):
                            continue
                        if len(part_4) > 1 and part_4.startswith('0'):
                            continue
                        rip = ip.copy()
                        rip.extend([part_3, part_4])
                        result.append('.'.join(rip))
                        flag = True
                return flag
        result = []
        split(s, 3, [], result)
        return result
        