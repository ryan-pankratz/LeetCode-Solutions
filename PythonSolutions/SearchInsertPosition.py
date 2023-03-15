class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def searchInsertHelper(self, nums: List[int], target: int, begin_index: int) -> int:
            if len(nums) == 1:
                if nums[0] == target or nums[0] > target:
                    return begin_index
                else:
                    return begin_index + 1
            else:
                mid = len(nums) // 2
                if nums[mid] > target:
                    return searchInsertHelper(self, nums[:mid], target, begin_index)
                elif nums[mid] < target:
                    return searchInsertHelper(self, nums[mid:], target, begin_index + mid)
                else:
                    return begin_index + mid
        return searchInsertHelper(self, nums, target, 0)