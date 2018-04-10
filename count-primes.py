"""
https://leetcode.com/submissions/detail/149213130/

Description:
Count the number of prime numbers less than a non-negative number, n.

Credits:Special thanks to @mithmatt for adding this problem and creating all test cases."""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]:
            return 0
       
        is_primes = [1] * n
        is_primes[0:2] = [0, 0]
        
        for i in range(2, int(n ** 0.5) + 1):
            is_primes[i * 2: : i] = [0] * len(is_primes[i * 2::i])
        return sum(is_primes)
        
        
        