"""
https://leetcode.com/submissions/detail/149517800/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.

```
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def string_xor(s1, s2):
            return str(int(s1) ^ int(s2))

        def string_and(s1, s2):
            if s1 == s2 and s1 == '1':
                return '1'
            return '0'

        def string_or(s1, s2):
            if s1 == '1' or s2 == '1':
                return '1'
            return '0'

        def add(a_bin, b_bin):
            flag = '0'
            result = []
            for a_bit, b_bit in list(zip(a_bin, b_bin))[::-1]:
                bit_sum = string_xor(string_xor(a_bit, b_bit), flag)
                result.insert(0, bit_sum)
                flag = string_or(string_or(string_and(a_bit, b_bit), string_and(a_bit, flag)), string_and(b_bit, flag))
            return ''.join(result)

        def reverse(n_bit):
            s = []
            for bit in n_bit:
                s.append('0' if bit == '1' else '1')
            return ''.join(s)

        def left_pad(n):
            result = []
            if n >= 0:
                n_bin = bin(n)[2:]
            else:
                n_bin = add(reverse(left_pad(abs(n))), left_pad(1))
            result = ['0'] * (32 - len(n_bin))
            result.append(n_bin)
            return ''.join(result)

        a_bin = left_pad(a)
        b_bin = left_pad(b)
        result = add(a_bin, b_bin)
        if result[0] == '0':
            return int(result, 2)
        result = add(reverse(result), left_pad(1))
        return -int(result, 2)
```

I operate `a` and `b` really bit by bit. I know I can use `(a >> n) & 1` to get the bit of position n from right to left. But I dont do it because I find it is so strange to represent negative in Python.

For example, number `-5` in Python is:

```
>>> bin(-5)
'-0b101'
```

but what I need is `0b11111111111111111111111111111011`. However, when I shift `-5` bit to bit, the output looks correct:

```
>>> (-5) & 1
1
>>> (-5 >> 1) & 1
1
>>> (-5 >> 2) & 1
0
>>> (-5 >> 3) & 1
1
>>> (-5 >> 4) & 1
1
>>> (-5 >> 5) & 1
1
>>> (-5 >> 6) & 1
1
>>> (-5 >> 7) & 1
1
```
looks from the output, `-5` in fact is `0b11111111111111111111111111111011`, but this may make people confused and hard to understand the 2-compliment for negative number.

Therefore, I just use string type of binary number to finish this problem.

I know the time is wasted in type transformtion, but It is more readable.
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def string_xor(s1, s2):
            return str(int(s1) ^ int(s2))

        def string_and(s1, s2):
            if s1 == s2 and s1 == '1':
                return '1'
            return '0'

        def string_or(s1, s2):
            if s1 == '1' or s2 == '1':
                return '1'
            return '0'

        def add(a_bin, b_bin):
            flag = '0'
            result = []
            for a_bit, b_bit in list(zip(a_bin, b_bin))[::-1]:
                bit_sum = string_xor(string_xor(a_bit, b_bit), flag)
                result.insert(0, bit_sum)
                flag = string_or(string_or(string_and(a_bit, b_bit), string_and(a_bit, flag)), string_and(b_bit, flag))
            return ''.join(result)

        def reverse(n_bit):
            s = []
            for bit in n_bit:
                s.append('0' if bit == '1' else '1')
            return ''.join(s)

        def left_pad(n):
            result = []
            if n >= 0:
                n_bin = bin(n)[2:]
            else:
                n_bin = add(reverse(left_pad(abs(n))), left_pad(1))
            result = ['0'] * (32 - len(n_bin))
            result.append(n_bin)
            return ''.join(result)

        a_bin = left_pad(a)
        b_bin = left_pad(b)
        result = add(a_bin, b_bin)
        if result[0] == '0':
            return int(result, 2)
        result = add(reverse(result), left_pad(1))
        return -int(result, 2)
