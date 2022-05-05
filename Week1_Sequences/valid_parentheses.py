"""
20. Valid Parentheses [Easy]
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
   * Open brackets must be closed by the same type of brackets.
   * Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        valid_pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        results = []
        for char in s:
            try:
                if results and char == valid_pairs[results[-1]]:
                    results.pop()
                else:
                    results.append(char)
            except KeyError:
                return False

        return len(results) == 0


if __name__ == "__main__":
    assert Solution.isValid(None, s="()") == True
    assert Solution.isValid(None, s="()[]{}") == True
    assert Solution.isValid(None, s="(]") == False
    assert Solution.isValid(None, s="){") == False
    assert Solution.isValid(None, s="({[)") == False
