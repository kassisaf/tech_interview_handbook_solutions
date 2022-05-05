"""
1. Two Sum [Easy]
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
  target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    return [i, j]


if __name__ == "__main__":
    assert Solution.twoSum(None, nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert Solution.twoSum(None, nums=[3, 2, 4], target=6) == [1, 2]
    assert Solution.twoSum(None, nums=[3, 3], target=6) == [0, 1]
