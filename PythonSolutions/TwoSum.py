from __future__ import annotations
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            required_num = target - nums[i]
            if required_num in d:
                return [d[required_num], i]
            d[nums[i]] = i