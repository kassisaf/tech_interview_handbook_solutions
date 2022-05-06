"""
53. Maximum Subarray [Easy]
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Runtime: 733 ms, faster than 92.19% of Python3 online submissions for Maximum Subarray.
"""
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = 0
        max_global = -sys.maxsize

        # Kadane's algorithm
        for num in nums:
            if max_current >= 0:
                max_current += num
            else:
                max_current = num

            if max_current > max_global:
                max_global = max_current

        return max_global


if __name__ == "__main__":
    assert Solution.maxSubArray(None, nums=[-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert Solution.maxSubArray(None, nums=[1]) == 1
    assert Solution.maxSubArray(None, nums=[5,4,-1,7,8]) == 23
    assert Solution.maxSubArray(None, nums=[-1]) == -1
    assert Solution.maxSubArray(None, nums=[-2,-1]) == -1
