from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums) // 2

        if len(nums) <= 1:
            if nums[index] == target:
                return index
            else:
                return -1

        if nums[index] == target:
            return index
        elif nums[index] < target:
            val = self.search(nums[index:], target)
            if val == -1:
                return -1
            return index + val
        else:
            return self.search(nums[0:index], target)