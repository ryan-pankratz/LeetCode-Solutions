#
# A solution file for the LeetCode Container with most water problem in Python.
#

from typing import List

def min(a, b):
    if a > b:
        return b
    return a

class Solution:
    def maxArea(self, height: List[int]) -> int:
        k = 0
        l = len(height) - 1
        maxArea = 0

        while (k != l):
            if maxArea < min(height[k], height[l]) * (l - k):
                maxArea = min(height[k], height[l]) * (l - k)
            
            if height[k] < height[l]:
                k += 1
            else:
                l -= 1
        return maxArea
