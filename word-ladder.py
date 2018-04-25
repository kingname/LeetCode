"""
https://leetcode.com/submissions/detail/151507325/

Given two words (beginWord and endWord), and a dictionary&#39;s word list, find the length of shortest transformation sequence from beginWord to endWord, such that:


	Only one letter can be changed at a time.
	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.


Note:


	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.


Example 1:


Input:
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

Output: 5

Explanation: As one shortest transformation is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,
return its length 5.


Example 2:


Input:
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

Output:&nbsp;0

Explanation:&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible&nbsp;transformation.




"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordSet.discard(beginWord)
        taskQueue = [(beginWord, 1)]
        while taskQueue:
            begin, path = taskQueue.pop(0)
            if begin == endWord:
                return path
            for i in range(len(begin)):
                for k in 'qwertyuiopasdfghjklzxcvbnm':
                    nextWord = begin[:i] + k + begin[i + 1:]
                    if nextWord in wordSet:
                        wordSet.discard(nextWord)
                        taskQueue.append((nextWord, path + 1))
        return 0