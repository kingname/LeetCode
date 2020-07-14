"""
https://leetcode.com/submissions/detail/366525549/

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called &quot;bulls&quot;) and how many digits match the secret number but locate in the wrong position (called &quot;cows&quot;). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend&#39;s guess, use A to indicate the bulls and B to indicate the cows.&nbsp;

Please note that both secret number and friend&#39;s guess may contain duplicate digits.

Example 1:


Input: secret = &quot;1807&quot;, guess = &quot;7810&quot;

Output: &quot;1A3B&quot;

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:


Input: secret = &quot;1123&quot;, guess = &quot;0111&quot;

Output: &quot;1A1B&quot;

Explanation: The 1st 1 in friend&#39;s guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend&#39;s guess only contain digits, and their lengths are always equal."""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess:
            return ''
        a_count = 0
        b_count = 0
        guess_list = list(guess)
        secret_index_dict = {}
        for index, s in enumerate(secret):
            if guess[index] == s:
                a_count += 1
                guess_list[index] = 'x'
            else:
                secret_index_dict.setdefault(s, set())
                secret_index_dict[s].add(index)
            
        for index, g in enumerate(guess_list):
            if g == 'x':
                continue
            if secret_index_dict.get(g):
                b_count += 1
                secret_index_dict[g].pop()
        return '{}A{}B'.format(a_count, b_count)
                