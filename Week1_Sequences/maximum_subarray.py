"""
53. Maximum Subarray [Easy]
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    assert Solution.maxSubArray(None, nums=[-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert Solution.maxSubArray(None, nums=[1]) == 1
    assert Solution.maxSubArray(None, nums=[5,4,-1,7,8]) == 23
