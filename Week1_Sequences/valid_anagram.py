"""
242. Valid Anagram [Easy]
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
  original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


if __name__ == "__main__":
    assert Solution.isAnagram(None, s="anagram", t="nagaram") == True
    assert Solution.isAnagram(None, s="rat", t="car") == False
