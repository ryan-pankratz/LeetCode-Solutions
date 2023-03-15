from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            return self._intersectionHelper(nums1, nums2)
        else:
            return self._intersectionHelper(nums2, nums1)

    def _intersectionHelper(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Precondtion: len(nums1) <= len(nums2)
        """
        ret_val = []
        for num in nums1:
            if num in nums2 and num not in ret_val:
                ret_val.append(num)

        return ret_val