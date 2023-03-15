class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums) - 1
        while count >= 0 and nums[count] == val:
            nums[count] = None
            count -= 1

        i = 0
        while i <= count:
            if nums[i] == val:
                if count == i:
                    nums[i] = None
                else:
                    nums[i] = nums[count]
                count -= 1
            else:
                i += 1

        return count + 1